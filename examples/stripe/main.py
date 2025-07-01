import os
import stripe
import air
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

# Initialize password hasher - best practice to use a proper password hasher
ph = PasswordHasher()

# In-memory user store (in production, use a proper database)
users = {}

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "dev-secret-key"))


@app.get("/", response_class=air.TagResponse)
async def index(request: Request):
    username = request.session.get("username")

    if username:
        body = (
            air.H1(f"Welcome, {username}"),
            air.Form(
                air.Button("Create Payment Session", type="submit"),
                action="/create-checkout-session",
                method="post"
            ),
            air.A("Protected Content", href="/protected"),
            air.Br(),
            air.A("Logout", href="/logout")
        )
    else:
        body = (air.H1("Please Login"), 
                air.A("Login", href="/login"))
    
    return air.Html(
        air.Head(air.Title("Stripe Example")), 
        air.Body(*body))


@app.get("/login", response_class=air.TagResponse)
async def login_form():
    return air.Html(
        air.Head(air.Title("Login")),
        air.Body(
            air.H1("Login"),
            air.Form(
                air.Label("Username:", for_="username"),
                air.Input(type="text", name="username", id="username", required=True),
                air.Br(),
                air.Label("Password:", for_="password"),
                air.Input(type="password", name="password", id="password", required=True),
                air.Br(),
                air.Button("Login", type="submit"),
                action="/login",
                method="post"
            ),
            air.Hr(),
            air.P("Don't have an account? ", air.A("Register", href="/register"))
        )
    )


@app.post("/login")
async def login(request: Request, username: str = Form(), password: str = Form()):
    if username not in users:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    try:
        ph.verify(users[username]["password_hash"], password)
        request.session["username"] = username
        return RedirectResponse("/", status_code=303)
    except VerifyMismatchError:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/register", response_class=air.TagResponse)
async def register_form():
    return air.Html(
        air.Head(air.Title("Register")),
        air.Body(
            air.H1("Register"),
            air.Form(
                air.Label("Username:", for_="username"),
                air.Input(type="text", name="username", id="username", required=True),
                air.Br(),
                air.Label("Password:", for_="password"),
                air.Input(type="password", name="password", id="password", required=True),
                air.Br(),
                air.Button("Register", type="submit"),
                action="/register",
                method="post"
            ),
            air.Hr(),
            air.P("Already have an account? ", air.A("Login", href="/login"))
        )
    )


@app.post("/register")
async def register(request: Request, username: str = Form(), password: str = Form()):
    if username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Hash the password before storing
    users[username] = {
        "password_hash": ph.hash(password),
        "has_subscription": False
    }
    
    # Log the user in immediately after registration
    request.session["username"] = username
    return RedirectResponse("/", status_code=303)


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


@app.get("/protected", response_class=air.TagResponse)
async def protected(request: Request):
    username = request.session.get("username")
    if not username or username not in users:
        return RedirectResponse("/login", status_code=303)
    
    # Check if user has active subscription
    has_subscription = users[username].get("has_subscription", False)
    
    if has_subscription:
        body = (
            air.H1("Protected Content"),
            air.P("You have an active subscription!"),
            air.P("This content is only available to subscribers."),
            air.A("Back to Home", href="/")
        )
    else:
        body = (
            air.H1("Subscription Required"),
            air.P("You need an active subscription to access this content."),
            air.Form(
                air.Button("Subscribe Now", type="submit"),
                action="/create-checkout-session",
                method="post"
            ),
            air.A("Back to Home", href="/")
        )
    
    return air.Html(
        air.Head(air.Title("Protected Content")),
        air.Body(*body)
    )


@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    username = request.session.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Example Product',
                    },
                    'unit_amount': 2000,  # $20.00
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=str(request.url_for('success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=str(request.url_for('cancel')),
            client_reference_id=username,  # Store username for webhook
        )
        return RedirectResponse(checkout_session.url, status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/success", response_class=air.TagResponse)
async def success(request: Request, session_id: str):
    return air.Html(
        air.Head(air.Title("Payment Success")),
        air.Body(
            air.H1("Payment Successful!"),
            air.P(f"Session ID: {session_id}"),
            air.P("Your subscription will be activated shortly."),
            air.P("If you don't see access within a few seconds, please refresh the page."),
            air.A("View Protected Content", href="/protected"),
            air.Br(),
            air.A("Back to Home", href="/")
        )
    )


@app.get("/cancel", response_class=air.TagResponse)
async def cancel():
    return air.Html(
        air.Head(air.Title("Payment Cancelled")),
        air.Body(
            air.H1("Payment Cancelled"),
            air.A("Back to Home", href="/")
        )
    )


@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"Payment completed for session: {session['id']}")
        
        # Get username from client_reference_id
        username = session.get('client_reference_id')
        if username and username in users:
            users[username]["has_subscription"] = True
            print(f"Subscription activated for user: {username}")
    
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
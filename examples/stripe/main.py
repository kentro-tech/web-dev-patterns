import os
import stripe
import air
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

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
            )
        )
    )


@app.post("/login")
async def login(request: Request, username: str = Form(), password: str = Form()):
    if password == "password":
        request.session["username"] = username
        return RedirectResponse("/", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Invalid password")


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    if not request.session.get("username"):
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
            success_url=request.url_for('success') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.url_for('cancel'),
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
    
    return {"status": "success"}
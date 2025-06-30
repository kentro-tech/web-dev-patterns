import os
import air
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from itsdangerous import URLSafeTimedSerializer, BadTimeSignature, SignatureExpired
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "dev-secret-key"))

serializer = URLSafeTimedSerializer(os.getenv("TOKEN_SECRET"))
sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

FROM_EMAIL = os.getenv("FROM_EMAIL")
APP_URL = os.getenv("APP_URL", "http://localhost:8000")


@app.get("/", response_class=air.TagResponse)
async def index(request: Request):
    email = request.session.get("email")
    
    return air.Html(
        air.Head(air.Title("Magic Link Auth Example")),
        air.Body(
            air.H1(f"Welcome, {email}"),
            air.P("You are logged in." if email else "You are not logged in."),
            air.A("View Protected Content", href="/protected") if email else '',
            air.Br() if email else '',
            air.A("Logout", href="/logout") if email else air.A("Login", href="/login")
        )
    )


@app.get("/login", response_class=air.TagResponse)
async def login_form():
    return air.Html(
        air.Head(air.Title("Login")),
        air.Body(
            air.H1("Login with Magic Link"),
            air.P("Enter your email address to receive a login link."),
            air.Form(
                air.Label("Email:", for_="email"),
                air.Input(type="email", name="email", id="email", required=True),
                air.Button("Send Magic Link", type="submit"),
                action="/login",
                method="post"
            )
        )
    )


@app.post("/login")
async def send_magic_link(email: str = Form()):
    token = serializer.dumps({"email": email, "timestamp": datetime.utcnow().isoformat()})
    magic_link = f"{APP_URL}/auth/verify?token={token}"
    
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=email,
        subject="Your Login Link",
        html_content=f"""
        <h2>Login to Your Account</h2>
        <p>Click the link below to login:</p>
        <p><a href="{magic_link}">Login Now</a></p>
        <p>This link will expire in 15 minutes.</p>
        <p>If you didn't request this, please ignore this email.</p>
        """
    )
    
    try:
        sg.send(message)
        return RedirectResponse("/login/sent", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send email")


@app.get("/login/sent", response_class=air.TagResponse)
async def login_sent():
    return air.Html(
        air.Head(air.Title("Check Your Email")),
        air.Body(
            air.H1("Check Your Email"),
            air.P("We've sent you a login link. Please check your email and click the link to continue."),
            air.P("The link will expire in 15 minutes."),
            air.A("Back to Home", href="/")
        )
    )


@app.get("/auth/verify")
async def verify_token(request: Request, token: str):
    try:
        data = serializer.loads(token, max_age=900)  # 15 minutes
        email = data["email"]
        
        # Create session
        request.session["email"] = email
        request.session["logged_in_at"] = datetime.utcnow().isoformat()
        
        return RedirectResponse("/", status_code=303)
        
    except SignatureExpired:
        raise HTTPException(status_code=400, detail="Link has expired")
    except BadTimeSignature:
        raise HTTPException(status_code=400, detail="Invalid link")


@app.get("/protected", response_class=air.TagResponse)
async def protected(request: Request):
    email = request.session.get("email")
    
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    logged_in_at = request.session.get("logged_in_at", "Unknown")
    
    return air.Html(
        air.Head(air.Title("Protected Content")),
        air.Body(
            air.H1("Protected Content"),
            air.P(f"Hello, {email}!"),
            air.P("This page is only accessible to authenticated users."),
            air.P(f"You logged in at: {logged_in_at}"),
            air.Hr(),
            air.A("Back to Home", href="/")
        )
    )


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

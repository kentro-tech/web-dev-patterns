# Air Web App Starter - LLM Quick Reference

## Core Setup

```bash
# Project setup
uv venv
source .venv/bin/activate  # Always activate before running
uv sync                     # Install from pyproject.toml
fastapi dev main.py         # Run with auto-reload
```

## Basic Air App

```python
import air
from fastapi import FastAPI

app = FastAPI()  # or app = air.Air() for HTML-only

@app.get("/", response_class=air.TagResponse)
async def index():
    return air.Html(
        air.Head(air.Title("My App")),
        air.Body(
            air.H1("Hello World"),
            air.P("Content here")
        )
    )
```

## Session-Based Auth Pattern

```python
from starlette.middleware.sessions import SessionMiddleware
from itsdangerous import URLSafeTimedSerializer

# Setup
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET"))
serializer = URLSafeTimedSerializer(os.getenv("TOKEN_SECRET"))

# Magic link flow
@app.post("/login")
async def send_magic_link(email: str = Form()):
    token = serializer.dumps({"email": email})
    # Send token via SendGrid/SMTP
    
@app.get("/auth/verify")
async def verify_token(request: Request, token: str):
    data = serializer.loads(token, max_age=900)  # 15 min
    request.session["email"] = data["email"]
    return RedirectResponse("/")

# Protected routes
@app.get("/protected")
async def protected(request: Request):
    if not request.session.get("email"):
        return RedirectResponse("/login")
    # Show protected content
```

## Stripe Integration Pattern

```python
import stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.post("/create-checkout-session")
async def create_checkout(request: Request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Product'},
                'unit_amount': 2000,  # $20.00
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=str(request.url_for('success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=str(request.url_for('cancel')),
    )
    return RedirectResponse(session.url)

# Webhook for payment confirmation
@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get('stripe-signature')
    event = stripe.Webhook.construct_event(payload, sig, webhook_secret)
    
    if event['type'] == 'checkout.session.completed':
        # Update user's subscription status
```

## Environment Management

```bash
# .env file (never commit)
SESSION_SECRET=<use: python -c "import secrets; print(secrets.token_urlsafe(32))">
TOKEN_SECRET=<same as above>
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
SENDGRID_API_KEY=SG...
FROM_EMAIL=noreply@example.com
APP_URL=http://localhost:8000
```

```python
# Load in main.py
from dotenv import load_dotenv
load_dotenv()
```

## Project Structure

```
myapp/
├── .env              # Secrets (gitignored)
├── .env.example      # Template for developers
├── pyproject.toml    # Dependencies via UV
├── main.py           # FastAPI app
└── uv.lock          # Locked dependencies
```

## pyproject.toml Template

```toml
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = [
    "fastapi",
    "air",
    "python-multipart",    # For Form() handling
    "python-dotenv",       # Environment vars
    "sendgrid",           # Magic link emails
    "itsdangerous",       # Token signing
    "stripe",             # Payments
]

[tool.uv]
dev-dependencies = [
    "pytest",
    "httpx",
]
```

## Common Patterns

### Forms
```python
air.Form(
    air.Input(type="email", name="email", required=True),
    air.Button("Submit", type="submit"),
    action="/submit",
    method="post"
)
```

### Conditional Content
```python
if request.session.get("user"):
    content = air.A("Logout", href="/logout")
else:
    content = air.A("Login", href="/login")
```

### Custom Components
```python
def card(header: str, *content):
    return air.Article(
        air.Header(header),
        *content
    )
```

## Quick Commands

```bash
# Add packages
uv add package-name
uv add --dev pytest

# Run tests
pytest

# Stripe webhook testing
stripe listen --forward-to localhost:8000/webhook

# Generate secrets
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
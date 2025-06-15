from fastapi import FastAPI, Depends, HTTPException, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import hashlib
import stripe
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv('../.env')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Configure Stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
print(f"STRIPE_WEBHOOK_SECRET: {STRIPE_WEBHOOK_SECRET}")
print(f"STRIPE_PUBLISHABLE_KEY: {os.getenv('STRIPE_PUBLISHABLE_KEY')}")
# Simple in-memory storage (use database in production)
users = {}
todos = {}
user_sessions = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize with sample users for testing
users["registered-user"] = {
    "password": hash_password("password"),
    "subscribed": False
}
users["subscribed-user"] = {
    "password": hash_password("password"), 
    "subscribed": True
}

# Initialize todos for sample users
todos["registered-user"] = []
todos["subscribed-user"] = [
    {"text": "Sample todo 1", "done": False},
    {"text": "Completed sample todo", "done": True},
    {"text": "Another todo item", "done": False}
]

def get_current_user(request: Request) -> Optional[str]:
    session_id = request.cookies.get("session_id")
    return user_sessions.get(session_id)

def require_auth(request: Request) -> str:
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    user = get_current_user(request)
    if not user:
        return templates.TemplateResponse("login.html", {"request": request})
    
    user_todos = todos.get(user, [])
    user_subscribed = users.get(user, {}).get("subscribed", False)
    return templates.TemplateResponse("todos.html", {
        "request": request, 
        "todos": user_todos,
        "user": user,
        "user_subscribed": user_subscribed
    })

@app.get("/premium", response_class=HTMLResponse)
async def premium(request: Request):
    user = require_auth(request)
    if not users[user]["subscribed"]:
        return RedirectResponse(url="/", status_code=303)
    
    return templates.TemplateResponse("premium.html", {
        "request": request,
        "user": user
    })

@app.post("/register")
async def register(username: str = Form(), password: str = Form()):
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    
    users[username] = {
        "password": hash_password(password),
        "subscribed": False
    }
    todos[username] = []
    return RedirectResponse(url="/", status_code=303)

@app.post("/login")
async def login(username: str = Form(), password: str = Form()):
    user = users.get(username)
    if not user or user["password"] != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    session_id = hashlib.sha256(f"{username}{password}".encode()).hexdigest()
    user_sessions[session_id] = username
    
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie("session_id", session_id)
    return response

@app.post("/logout")
async def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id in user_sessions:
        del user_sessions[session_id]
    
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("session_id")
    return response

@app.post("/todos")
async def add_todo(request: Request, todo: str = Form()):
    user = require_auth(request)
    if not users[user]["subscribed"]:
        raise HTTPException(status_code=403, detail="Subscription required")
    
    if user not in todos:
        todos[user] = []
    todos[user].append({"text": todo, "done": False})
    return RedirectResponse(url="/", status_code=303)

@app.post("/todos/{todo_id}/toggle")
async def toggle_todo(request: Request, todo_id: int):
    user = require_auth(request)
    if 0 <= todo_id < len(todos[user]):
        todos[user][todo_id]["done"] = not todos[user][todo_id]["done"]
    return RedirectResponse(url="/", status_code=303)

@app.get("/subscribe", response_class=HTMLResponse)
async def subscribe_page(request: Request):
    user = require_auth(request)
    return templates.TemplateResponse("subscribe.html", {
        "request": request,
        "user": user,
        "stripe_publishable_key": os.getenv("STRIPE_PUBLISHABLE_KEY")
    })

@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    user = require_auth(request)
    print(f"STRIPE_PRICE_ID: {os.getenv('STRIPE_PRICE_ID')}")
    checkout_session = stripe.checkout.Session.create(
        line_items=[{
            'price': os.getenv("STRIPE_PRICE_ID"),
            'quantity': 1,
        }],
        mode='subscription',
        success_url=request.url_for("subscription_success"),
        cancel_url=request.url_for("root"),
        metadata={'username': user}
    )
    return RedirectResponse(url=checkout_session.url, status_code=303)

@app.get("/subscription-success")
async def subscription_success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})

@app.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        username = session['metadata']['username']
        if username in users:
            users[username]["subscribed"] = True
    
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


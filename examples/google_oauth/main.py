import os
from typing import Optional
from dotenv import load_dotenv
import air
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET"))

oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@app.get("/", response_class=air.TagResponse)
async def index(request: Request):
    user = request.session.get('user')
    
    return air.Html(
        air.Head(
            air.Title("Google OAuth Example"),
            air.Style("""
                body { 
                    font-family: system-ui; 
                    max-width: 600px; 
                    margin: 50px auto; 
                    padding: 20px;
                }
                .button {
                    display: inline-block;
                    background: #4285f4;
                    color: white;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 4px;
                    margin: 10px 0;
                }
                .user-info {
                    background: #f0f0f0;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 20px 0;
                }
            """)
        ),
        air.Body(
            air.H1("Google OAuth Example"),
            
            air.Div(
                air.H2(f"Welcome, {user['name']}!"),
                air.P(f"Email: {user['email']}"),
                air.Img(src=user['picture'], alt="Profile", style="width: 100px; border-radius: 50%;"),
                air.Br(),
                air.A("Logout", href="/logout", class_="button"),
                class_="user-info"
            ) if user else air.Div(
                air.P("You are not logged in."),
                air.A("Login with Google", href="/login", class_="button")
            )
        )
    )

@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get("/auth")
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get('userinfo')
    
    if user_info:
        request.session['user'] = {
            'name': user_info.get('name'),
            'email': user_info.get('email'),
            'picture': user_info.get('picture')
        }
    
    return RedirectResponse(url='/')

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url='/')

@app.get("/protected", response_class=air.TagResponse)
async def protected(request: Request):
    user = request.session.get('user')
    
    if not user:
        return RedirectResponse(url='/login')
    
    return air.Html(
        air.Head(air.Title("Protected Page")),
        air.Body(
            air.H1("Protected Content"),
            air.P(f"This page is only visible to authenticated users."),
            air.P(f"Hello, {user['name']}!"),
            air.A("Back to Home", href="/")
        )
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
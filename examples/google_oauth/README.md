# Minimal Google OAuth Example

A minimal example of Google OAuth authentication using FastAPI and Air.

## Setup

1. **Install dependencies:**
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

2. **Configure Google OAuth:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing
   - Enable Google+ API
   - Create OAuth 2.0 credentials (Web application)
   - Add authorized redirect URI: `http://localhost:8000/auth`

3. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Google credentials
   ```

4. **Generate session secret:**
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   # Add to .env as SESSION_SECRET
   ```

5. **Run the app:**
   ```bash
   fastapi dev main.py
   ```

## Features

- Login with Google
- Session-based authentication
- Protected routes
- User profile display
- Logout functionality

## Routes

- `/` - Home page (shows login or user info)
- `/login` - Initiates Google OAuth flow
- `/auth` - OAuth callback endpoint
- `/logout` - Clears session
- `/protected` - Example protected route
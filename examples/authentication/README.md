# Magic Link Authentication Example

Minimal magic link authentication using SendGrid SMTP.

## Quick Start

```bash
cd examples/authentication
uv venv
source .venv/bin/activate

# Install dependencies
uv sync

# Set up environment
cp .env.example .env
# Edit .env with your SendGrid API key

# Run
fastapi dev main.py
```

## Get SendGrid API Key

1. Sign up at https://sendgrid.com
2. Create API key at https://app.sendgrid.com/settings/api_keys
3. Verify sender email in SendGrid

## Routes

- `/` - Home page showing auth status
- `/login` - Email entry for magic link
- `/auth/verify` - Magic link verification
- `/logout` - Clear session

## How It Works

1. User enters email
2. System sends magic link via SendGrid
3. User clicks link (expires in 15 minutes)
4. System creates session
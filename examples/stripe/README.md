# Stripe Integration Example

Minimal Stripe payment integration with session-based authentication.

## Quick Start

```bash
cd examples/stripe
uv venv
source .venv/bin/activate

# Install dependencies
uv sync

# Set up environment
cp .env.example .env
# Edit .env with your Stripe keys

# Generate a secure SESSION_SECRET:
python -c "import secrets; print(secrets.token_urlsafe(32))"
# Copy the output to SESSION_SECRET in .env

# Get webhook secret and create listener 
stripe listen --forward-to localhost:8000/webhook

# Run
fastapi dev main.py
```

## Routes

- `/` - Home page with login/payment options
- `/login` - Login form (password: `password`)
- `/protected` - Protected content (requires subscription)
- `/create-checkout-session` - Create Stripe payment
- `/success` - Payment success page
- `/webhook` - Stripe webhook endpoint
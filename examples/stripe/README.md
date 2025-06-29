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

# Run
fastapi dev main.py
```

## Get Stripe Keys

1. Sign up at https://stripe.com
2. Get test keys from https://dashboard.stripe.com/test/apikeys
3. For webhooks locally:
```bash
stripe listen --forward-to localhost:8000/webhook
```

## Routes

- `/` - Home page with login/payment options
- `/login` - Login form (password: `password`)
- `/create-checkout-session` - Create Stripe payment
- `/success` - Payment success page
- `/webhook` - Stripe webhook endpoint
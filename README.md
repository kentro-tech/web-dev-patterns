# Minimal Todo App with FastAPI and Stripe

A minimal todo application demonstrating user authentication and Stripe subscription integration.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Stripe

1. Create a Stripe account at https://stripe.com
2. Go to your Stripe Dashboard
3. Get your API keys from the "Developers" > "API keys" section
4. Create a subscription product and price in "Products" section
5. Copy the Price ID

### 3. Configure Environment Variables

Copy `env.example` to `.env` and fill in your Stripe credentials:

```bash
cp env.example .env
```

Edit `.env` with your actual Stripe values:
- `STRIPE_SECRET_KEY`: Your secret key (starts with `sk_test_` or `sk_live_`)
- `STRIPE_PUBLISHABLE_KEY`: Your publishable key (starts with `pk_test_` or `pk_live_`)
- `STRIPE_PRICE_ID`: The price ID of your subscription product (starts with `price_`)
- `STRIPE_WEBHOOK_SECRET`: Webhook signing secret (see step 4)

### 4. Set Up Stripe Webhook (Local Development)

1. Install Stripe CLI: https://stripe.com/docs/stripe-cli
2. Login to Stripe CLI: `stripe login`
3. Forward events to your local server:
   ```bash
   stripe listen --forward-to localhost:8000/stripe-webhook
   ```
4. Copy the webhook signing secret from the CLI output
5. Add the webhook secret to your `.env` file as `STRIPE_WEBHOOK_SECRET`

### 5. Run the Application

```bash
cd fastapi
python main.py
```

Or with uvicorn directly:
```bash
uvicorn fastapi.main:app --reload
```

### 6. Usage

1. Go to http://localhost:8000
2. Register a new account
3. Login with your credentials
4. Subscribe to unlock todo functionality
5. Create and manage your todos

## Architecture

- **Authentication**: Simple session-based auth with password hashing
- **Storage**: In-memory storage (replace with database for production)
- **Payments**: Stripe Checkout for subscription management
- **Frontend**: Minimal HTML templates (no CSS framework)

## Production Notes

- Replace in-memory storage with a proper database
- Add proper session management (Redis, etc.)
- Implement proper error handling and validation
- Add rate limiting and security headers
- Use environment-specific configuration

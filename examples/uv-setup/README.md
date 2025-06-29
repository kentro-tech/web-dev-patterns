# UV Setup Example

A minimal example showing how to use UV for Python package management.

## Quick Start

### 1. Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

cd examples/uv-setup
uv venv
source .venv/bin/activate 

# Install all dependencies from pyproject.toml
uv sync

# Or add individual packages
uv add fastapi
uv add sqlalchemy
uv add air

# Edit .env with secrets
cp .env.example .env

# activate venv first before running
source .venv/bin/activate
fastapi dev main.py
```

## UV Commands Cheat Sheet

```bash
# Create virtual environment
uv venv

# Add a package
uv add package-name

# Add dev dependency
uv add --dev pytest

# Remove package
uv remove package-name

# Sync dependencies (install from pyproject.toml)
uv sync

# Update all packages
uv sync --upgrade

# Run command in venv
uv run python main.py
```

## Project Structure

```
uv-setup/
├── .env.example      # Environment variables template
├── .gitignore        # Git ignore file
├── pyproject.toml    # UV/Python project config
└── main.py           # Simple FastAPI hello world app
```

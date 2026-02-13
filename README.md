# Minimal Railway App

A minimal FastAPI app ready for Railway deployment.

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit http://localhost:8000

## Deploy to Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize
railway init

# Deploy
railway up
```

Railway will auto-detect Python from `requirements.txt` and build/run the app.

## Add Database (Optional)

```bash
railway add postgres
railway link
```

Then access `DATABASE_URL` env var in your app:

```python
import os
database_url = os.getenv("DATABASE_URL")
```

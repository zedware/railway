import os
from fastapi import FastAPI

app = FastAPI()

PORT = int(os.getenv("PORT", 8000))


@app.get("/")
async def root():
    return {"message": "Hello Railway!", "port": PORT}


@app.get("/health")
async def health():
    return {"status": "ok"}

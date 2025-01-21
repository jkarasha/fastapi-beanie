
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .database import init_db
from .routes.product_review import router as Router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to your Beanie powered app"}

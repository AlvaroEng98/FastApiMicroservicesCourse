from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import Migrator
from apps.routers import product

@asynccontextmanager
async def lifespan(app: FastAPI):
    Migrator().run()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
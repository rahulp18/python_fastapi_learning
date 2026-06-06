from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import select

from app.api.routes.auth import router as auth_router
from app.db.session import AsyncSessionLocal
from app.models import Permission
from app.seeds.permission_seed import seed_permissions


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Permission).limit(1))
        if result.scalar_one_or_none() is None:
            await seed_permissions(db)
    yield


app = FastAPI(
    title="Ai Workspace API",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"message": "API Running"}


app.include_router(auth_router)
# app.include_router(project_router)
 
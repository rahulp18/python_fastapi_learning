from fastapi import FastAPI
from app.api.routes.auth import router as auth_router
from app.api.routes.project import router as project_router
from app.db.base import Base
from app.db.session import engine

# Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Ai Workspace API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return{
        "message":"API Running"
    }

app.include_router(auth_router)
app.include_router(project_router)
 
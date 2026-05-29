from fastapi import FastAPI # type: ignore

from backend.api.auth_routes import router

from backend.database.db import engine
from backend.database.models import Base

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="AI Study Companion API"
)

app.include_router(router)

@app.get("/")
def home():

    return {
        "message":
        "API Running"
    }
from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.routers.health import router as health_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Autonomous Intelligent Employee Platform",
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": f"Welcome to {settings.app_name} 🚀"
    }


app.include_router(health_router)
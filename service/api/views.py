from fastapi import APIRouter, FastAPI

from .routes import healthcheck, recs

router = APIRouter()

def add_views(app: FastAPI) -> None:
    router.include_router(healthcheck.router, prefix="/health", tags=["health"])
    router.include_router(recs.router, prefix="/reco", tags=["recommendations"])
    app.include_router(router)
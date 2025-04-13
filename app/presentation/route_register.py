from fastapi import FastAPI

from app.presentation.hint.routes import router as hint_router
from app.presentation.level.routes import router as level_router
from app.presentation.service.routes import router as service_router


def register_routers(app: FastAPI) -> None:
    app.include_router(service_router, tags=["Service"])
    app.include_router(level_router, tags=["Level"])
    app.include_router(hint_router, tags=["Hints"])

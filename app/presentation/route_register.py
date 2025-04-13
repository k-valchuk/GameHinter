from fastapi import FastAPI

from app.presentation.hint.routes import router as hint_router
from app.presentation.level.routes import router as level_router


def register_routers(app: FastAPI) -> None:
    app.include_router(level_router, tags=["Level"])
    app.include_router(hint_router, tags=["Hints"])

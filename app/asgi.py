import sys

from fastapi import FastAPI
from loguru import logger

from app.core.level_storage import LevelStorage
from app.core.level_translator import LevelTranslator
from app.presentation.route_register import register_routers


class Application:

    def __init__(self) -> None:
        pass

    def __setup_logger(self) -> None:
        logger.remove()
        logger.add(sys.stdout, level="INFO")

    async def setup(self) -> FastAPI:
        self.__setup_logger()
        logger.info("Initialization..")
        app = FastAPI()
        level_storage = LevelStorage()
        level_translator = LevelTranslator()
        app.dependency_overrides[LevelStorage] = lambda: level_storage
        app.dependency_overrides[LevelTranslator] = lambda: level_translator
        app.state.level_storage = level_storage
        register_routers(app)
        logger.info("Initialization complete")
        return app

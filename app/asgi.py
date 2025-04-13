import sys

from fastapi import FastAPI
from loguru import logger

from app.config import config
from app.core.hint_worker import HintWorker
from app.core.level_storage import LevelStorage
from app.core.level_translator import LevelTranslator
from app.presentation.exceptions.setup import setup_exceptions_handlers
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
        hint_worker = HintWorker(config, level_storage, level_translator)
        app.dependency_overrides[LevelStorage] = lambda: level_storage
        app.dependency_overrides[HintWorker] = lambda: hint_worker
        setup_exceptions_handlers(app)
        register_routers(app)
        logger.info("Initialization complete")
        return app

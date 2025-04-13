import sys

from fastapi import FastAPI
from loguru import logger

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
        register_routers(app)
        logger.info("Initialization complete")
        return app

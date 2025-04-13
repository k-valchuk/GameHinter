from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from pydantic import ValidationError
from starlette import status


def setup_exceptions_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ValidationError, bad_level_exception_handler)

    app.add_exception_handler(KeyError, no_level_found_exception_handler)


async def bad_level_exception_handler(
    request: Request, exc: ValidationError
) -> PlainTextResponse:
    return PlainTextResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content="Уровень не может быть без игрока или без объектов",
    )


async def no_level_found_exception_handler(
    request: Request, exc: KeyError
) -> PlainTextResponse:
    return PlainTextResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content="Уровень не найден",
    )

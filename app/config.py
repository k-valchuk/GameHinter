import datetime
import pickle
from pathlib import Path

from fastapi import types
from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    OPENAI_API_KEY: str = Field(description="Ключ для получения доступа к API OpenAI")

    API_PREFIX: str = Field(default="/api/v1", description="Префикс API")


config = Config()

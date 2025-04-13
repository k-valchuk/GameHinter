import json

from fastapi import UploadFile

from app.application.interfaces.level_storage import ILevelStorage
from app.application.interfaces.models import Level


class LevelStorage(ILevelStorage):
    def __init__(self) -> None:
        self.__data: dict[int, Level] = {}

    def get_level(self, level_id: int) -> Level | None:
        return self.__data.get(level_id, None)

    def get_all_levels(self) -> list[Level]:
        return list(self.__data.values())

    async def create_level(self, level_data: UploadFile) -> None:
        json_data = await level_data.read()
        json_data = json.loads(json_data)
        level = Level.model_validate(json_data["level"])  # type: ignore
        self.__data[level.id] = level

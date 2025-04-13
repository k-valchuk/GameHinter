from abc import ABC, abstractmethod

from fastapi import UploadFile

from app.application.interfaces.models import Level


class ILevelStorage(ABC):

    @abstractmethod
    def get_level(self, level_id: int) -> Level:
        raise NotImplementedError

    @abstractmethod
    def get_all_levels(self) -> list[Level]:
        raise NotImplementedError

    @abstractmethod
    async def create_level(self, level_data: UploadFile) -> None:
        raise NotImplementedError

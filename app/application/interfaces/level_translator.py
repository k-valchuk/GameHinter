from abc import ABC, abstractmethod

from app.application.interfaces.models import Level


class ILevelTranslator(ABC):

    @abstractmethod
    async def translate_text(self, text: str, scr: str, dest: str) -> str:
        raise NotImplementedError

    @abstractmethod
    async def translate_level(self, level: Level) -> str:
        raise NotImplementedError

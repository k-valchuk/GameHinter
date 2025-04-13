import asyncio

from googletrans import Translator

from app.application.interfaces.level_translator import ILevelTranslator
from app.application.interfaces.models import Level


class LevelTranslator(ILevelTranslator):

    def __init__(self) -> None:
        self.__translator = Translator()

    async def translate_text(self, text: str, src: str = "en", dest: str = "ru") -> str:
        translation = await self.__translator.translate(text, src=src, dest=dest)
        return translation.text

    async def translate_level(self, level: Level) -> str:
        level_text = ""
        translated_objects = await asyncio.gather(
            *[self.translate_text(obj.type) for obj in level.objects]
        )
        for translated_object, coords in zip(
            translated_objects, [(obj.x, obj.y) for obj in level.objects]
        ):
            level_text += f"{translated_object} на ({coords[0]}, {coords[1]}), "
        return level_text[:-2]

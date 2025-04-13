from fastapi import APIRouter, Depends

from app.application.interfaces.level_storage import ILevelStorage
from app.application.interfaces.level_translator import ILevelTranslator
from app.config import config
from app.core.level_storage import LevelStorage
from app.core.level_translator import LevelTranslator
from app.utils.stub import Stub

router = APIRouter(prefix=f"{config.API_PREFIX}/hints")


@router.get("/{level_id}")
async def get_hint(
    level_id: int,
    level_translator: ILevelTranslator = Depends(Stub(LevelTranslator)),
    level_storage: ILevelStorage = Depends(Stub(LevelStorage)),
):
    return await level_translator.translate_level(level_storage.get_level(level_id))

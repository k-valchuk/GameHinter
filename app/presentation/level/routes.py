from fastapi import APIRouter, Depends, File, UploadFile

from app.application.interfaces.level_storage import ILevelStorage
from app.application.interfaces.models import Level
from app.config import config
from app.core.level_storage import LevelStorage
from app.utils.stub import Stub

router = APIRouter(prefix=f"{config.API_PREFIX}/levels")


@router.get("", status_code=200)
async def get_levels(level_storage: ILevelStorage = Depends(Stub(LevelStorage))):
    """
    Endpoint для получения всех уровней

    Response: 200
    """
    return level_storage.get_all_levels()


@router.get("/{level_id}", status_code=200)
async def get_level(
    level_id: int, level_storage: ILevelStorage = Depends(Stub(LevelStorage))
) -> Level:
    """
    Endpoint для уровня по его id

    Response: 200

    Исключения:
    - HTTPException(`404`) - Уровень не найден
    """
    return level_storage.get_level(level_id)


@router.post("", status_code=201)
async def create_level(
    level_file: UploadFile = File(...),
    level_storage: ILevelStorage = Depends(Stub(LevelStorage)),
) -> int:
    """
    Endpoint для создания уровня, возвращает его id

    Response: 201

    Исключения:
    - HTTPException(`422`) - Уровень не может быть без игрока
    """

    return await level_storage.create_level(level_file)

from fastapi import APIRouter, Depends, File, Response, UploadFile

from app.application.interfaces.level_storage import ILevelStorage
from app.config import config
from app.core.level_storage import LevelStorage
from app.utils.stub import Stub

router = APIRouter(prefix=f"{config.API_PREFIX}/levels")


@router.get("")
async def get_levels(level_storage: ILevelStorage = Depends(Stub(LevelStorage))):
    """
    Endpoint для получения всех уровней

    Response: 200
    """
    return level_storage.get_all_levels()


@router.get("/{level_id}")
async def get_level(
    level_id: int, level_storage: ILevelStorage = Depends(Stub(LevelStorage))
):
    """
    Endpoint для уровня по его id

    Response: 200
    """
    return level_storage.get_level(level_id)


@router.post("")
async def create_level(
    level_file: UploadFile = File(...),
    level_storage: ILevelStorage = Depends(Stub(LevelStorage)),
):
    """
    Endpoint для создания уровня

    Response: 201
    """

    await level_storage.create_level(level_file)
    return Response(status_code=201)

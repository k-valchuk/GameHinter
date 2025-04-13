from fastapi import APIRouter, Depends

from app.application.interfaces.hint_worker import IHintWorker
from app.config import config
from app.core.hint_worker import HintWorker
from app.utils.stub import Stub

router = APIRouter(prefix=f"{config.API_PREFIX}/hints")


@router.get("/{level_id}")
async def get_hint(
    level_id: int,
    hint_worker: IHintWorker = Depends(Stub(HintWorker)),
) -> str:
    """
    Endpoint для получения подсказки

    Response: 200

    Исключения:
    - HTTPException(`404`) - Уровень не найден
    """
    return await hint_worker.generate_hint(level_id)

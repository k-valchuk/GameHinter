from fastapi import APIRouter

from app.config import config

router = APIRouter(prefix=f"{config.API_PREFIX}/hints")


@router.get("")
async def get_hint(level_id: int):
    return f"hint {level_id}"

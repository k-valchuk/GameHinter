from fastapi import APIRouter, HTTPException, Response

from app.config import config

router = APIRouter(prefix=f"{config.API_PREFIX}/hints")


@router.get("")
async def get_hint(level_id):
    return "hint"

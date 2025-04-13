from fastapi import APIRouter, Response

from app.config import config

router = APIRouter(prefix=f"{config.API_PREFIX}/config")


@router.get("")
async def get_config():
    return {}


@router.put("")
async def change_config():
    return Response(status_code=204)

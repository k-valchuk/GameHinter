from fastapi import APIRouter, HTTPException, Response

from app.config import config

router = APIRouter(prefix=f"{config.API_PREFIX}/levels")


@router.get("")
async def get_levels():
    return []


@router.get("/{level_id}")
async def get_level(level_id: int):
    return {}


@router.post("")
async def get_config():
    return Response(status_code=201)

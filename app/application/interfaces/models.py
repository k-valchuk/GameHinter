from pydantic import BaseModel


class LevelObject(BaseModel):
    type: str
    x: int
    y: int


class Level(BaseModel):
    id: int
    objects: list[LevelObject]

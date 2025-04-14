from pydantic import BaseModel, field_validator


class LevelObject(BaseModel):
    type: str
    x: int
    y: int


class Level(BaseModel):
    id: int
    objects: list[LevelObject]

    @field_validator("objects", mode="after")
    @classmethod
    def has_player(cls, value: list[LevelObject]) -> list[LevelObject]:
        if len(value) <= 1:
            raise ValueError
        for obj in value:
            if "player" in obj.type:
                return value
        raise ValueError


class Hint(BaseModel):
    id: int
    hint: str

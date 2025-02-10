from pydantic import BaseModel


class Species(BaseModel):
    name: str
    type: str
    size: str
    speed: int
    darkvision: int
    languages: list[str]

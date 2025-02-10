from pydantic import BaseModel


class Background(BaseModel):
    name: str
    descreption: str
    languages: list[str]
    proeficiencies: list[str]

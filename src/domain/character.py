from pstats import Stats
from typing import Optional

from pydantic import BaseModel

from domain.backgrounds import Background
from domain.classes import DndClass
from domain.species import Species
from domain.spells import Spell


class Character(BaseModel):
    name: str
    level: int
    dnd_class: DndClass
    species: Species
    languages: list[str]
    stats: Optional[Stats]
    spells = Optional[list[Spell]]
    background: Optional[Background]
    current_hp: Optional[int]
    temp_hp: Optional[int]
    _max_hp: Optional[int]

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from domain.feats import Feat


class DndClass(BaseModel):
    name: str
    _hit_die: int
    origin_feat: Optional[Feat]
    proficiencies: list[str]
    subclasses: Optional[Subclass]
    features: list[str]
    _spell_slots: list[int]


class Subclass(BaseModel):
    pass

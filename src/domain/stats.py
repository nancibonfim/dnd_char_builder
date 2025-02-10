from pydantic import BaseModel


class Stats(BaseModel):
    passive_perception: int
    passive_investigation: int
    passive_insight: int
    armor_class: int
    hit_points: int
    hit_dice: str
    speed: int
    initiative: int
    proficiency_bonus: int
    saving_throws: dict[str, int]
    skills: dict[str, int]
    resistances: list[str]
    immunities: list[str]
    vulnerabilities: list[str]
    condition_immunities: list[str]
    senses: dict[str, int]
    languages: list[str]

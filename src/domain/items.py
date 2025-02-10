from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    equipped: bool
    quantity: int
    body_slot: str
    weight: float
    type: str
    body_slot: str

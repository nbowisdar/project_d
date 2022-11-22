from typing import TypedDict


class ItemsForDed(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int


class ForGetProfileSchema(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int

from typing import NamedTuple


class BaseItemSchema(NamedTuple):
    link_dm: str


class ForGetFloatSchema(NamedTuple):
    link_dm: str
    in_game: str


class ItemsForGetFloatSchema(NamedTuple):
    items: list[ForGetFloatSchema]


class ForGetProfileSchema(NamedTuple):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int


# class ItemsForGetProfileSchema(BaseItemSchema):
#     items: list[ForGetProfileSchema]

from typing import NamedTuple


class BaseItemSchema(NamedTuple):
    link_dm: str


class ForGetFloatSchema(NamedTuple):
    link_dm: str
    in_game: str


class ItemsForGetFloatSchema(NamedTuple):
    items: list[ForGetFloatSchema]



# class ItemsForGetProfileSchema(BaseItemSchema):
#     items: list[ForGetProfileSchema]

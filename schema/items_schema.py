from pydantic import BaseModel


class BaseItemSchema(BaseModel):
    link_dm: str


class ForGetFloatSchema(BaseItemSchema):
    in_game: str


class ItemsForGetFloatSchema(BaseModel):
    items: list[ForGetFloatSchema]


class ForGetProfileSchema(BaseItemSchema):
    name: str
    float_value: float
    paint_seed: int


class ItemsForGetProfileSchema(BaseItemSchema):
    items: list[ForGetProfileSchema]

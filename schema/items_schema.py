from pydantic import BaseModel


class BaseItemSchema(BaseModel):
    link_dm: str


class ForGetFloatSchema(BaseItemSchema):
    in_game: str


class ForGetProfileSchema(BaseItemSchema):
    name: str
    float_value: float
    paint_seed: int

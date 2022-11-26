from typing import TypedDict
from typing import NamedTuple


class ForGetFloatSchema(NamedTuple):
    link_dm: str
    in_game: str


class ItemsForDed(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int
    profile_link: str | None
    trade_link: str | None


class ForGetProfileSchema(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int



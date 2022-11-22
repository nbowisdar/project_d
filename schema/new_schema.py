from typing import TypedDict
from typing import NamedTuple


class ItemsForDed(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int
    profile_link: str | None
    trade_link: str | None


class DedovResult(NamedTuple):
    profile_link: str
    trade_link: str | None


class ForGetProfileSchema(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int



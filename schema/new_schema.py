from typing import TypedDict


class ItemsForDed(TypedDict):
    link_dm: str
    name: str
    float_value: float
    paint_seed: int


# def test():
#     x = ItemsForDed(name='name', paint_seed='dwad', float_value='1232', link_dm='dsdas')
#     print(x['name'])

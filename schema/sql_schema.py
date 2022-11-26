from typing import TypedDict


class UserSchema(TypedDict):
    name: str
    profile: str
    trade_link: str | None


class ItemSchema(TypedDict):
    name: str
    dm_link: str
    user: UserSchema

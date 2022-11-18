from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    profile: str
    trade_link: str | None


class ItemSchema(BaseModel):
    name: str
    dm_link: str
    user: UserSchema

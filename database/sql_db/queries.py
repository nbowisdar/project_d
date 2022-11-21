from peewee import IntegrityError

from schema.sql_schema import ItemSchema, UserSchema
from setup import db
from tables import User, Item
from loguru import logger


def get_all() -> list[ItemSchema]:
    items = Item.select(User)
    rez = []
    for item in items:
        rez.append(ItemSchema(
            name=item.name,
            dm_link=item.dm_link,
            user=UserSchema(
                name=item.user.name,
                profile=item.user.profile,
                trade_link=item.user.trade_link
            )
        ))
    return rez


def add_item(item: ItemSchema) -> bool:
    try:
        Item.create(
            name=item.name,
            dm_link=item.dm_link,
            user=item.user
        )
        return True
    except IntegrityError:
        return False

from peewee import IntegrityError

from schema.sql_schema import ItemSchema, UserSchema
from setup import db
from tables import User, Item
from loguru import logger


def get_all() -> list[Item]:
    return Item.select(User)


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


if __name__ == '__main__':
    user = UserSchema(
        name='Vova',
        profile='my_prof',
        trade_link='http//:hello'
    )
    item = ItemSchema(name='hello', dm_link='123123', user=user)
    print(item)
    Item.create(**item.dict())
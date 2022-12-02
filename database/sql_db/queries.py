from peewee import IntegrityError
from schema.new_schema import ItemsForDed, ForGetFloatSchema, ForGetProfileSchema

from database.sql_db.setup import db
from database.sql_db.tables import User, Item, ItemFullData
from loguru import logger


def get_all() -> list[Item]:
    return Item.select(User)


def _save_user(profile_link: str, trade_link: str) -> User | None:
    try:
        if profile_link:
            with db.atomic():
                return User.get_or_create(profile=profile_link, trade_link=trade_link)
        return None
    except IntegrityError as err:
        logger.error(err)


def _save_item(item_name: str, dm_link: str, user: User = None):
    try:
        with db.atomic():
            Item.create(name=item_name, dm_link=dm_link, user=user[0])
    except IntegrityError as err:
        logger.error(err)


def save_item_in_db(item: ItemsForDed):
    current_user = _save_user(item['profile_link'], item['trade_link'])
    print(type(current_user))
    print(current_user)
    _save_item(
        item['name'], item['link_dm'], current_user
    )


def check_new(items: list[ForGetFloatSchema]) -> list[ForGetFloatSchema]:
    new_items = []
    old_items = ItemFullData.select()
    for item in items:
        exists = old_items.where(ItemFullData.link_dm == item.link_dm).get_or_none()
        if exists:
            continue
        new_items.append(item)
    return new_items


def save_only_items_in_db(items: list[ForGetProfileSchema]) -> bool:
    try:
        with db.atomic():
            for item in items:
                ItemFullData.create(
                    link_dm=item['link_dm'],
                    name=item['name'],
                    float_value=item['float_value'],
                    paint_seed=item['paint_seed']
                )
        return True
    except Exception as err:
        logger.info(err)
        return False


# def get_didovi_items() -> list[ForGetProfileSchema]:
#     items = ItemFullData.select()
#     for item in items:
#         yield ForGetProfileSchema(
#             link_dm=item.link_dm,
#             name=item.name,
#             float_value=item.float_value,
#             paint_seed=item.paint_seed
#         )

def get_didovi_items() -> list[ItemsForDed]:
    items = Item.select().where(Item.user is None)
    rez = []
    for item in items:
        rez.append(ItemsForDed(
            link_dm=item.link_dm,
            name=item.name,
            float_value=item.float_value,
            paint_seed=item.paint_seed
        ))
    return rez


#
# if __name__ == '__main__':
#     x = get_didovi_items()
#     print(x)
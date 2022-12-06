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


def _save_item(*, item_name: str, link_dm: str, user: tuple[User, bool]):
    try:
        with db.atomic():
            Item.create(name=item_name, link_dm=link_dm, user=user[0])
    except IntegrityError as err:
        logger.error(err)


def _set_is_parsed_true(link_dm: str):
    current_item = ItemFullData.get(link_dm=link_dm)
    current_item.is_parsed = True
    current_item.save()


def save_item_in_db(item: ItemsForDed):
    link_dm = item['link_dm']
    _set_is_parsed_true(link_dm)
    current_user = _save_user(item['profile_link'], item['trade_link'])
    _save_item(
        item_name=item['name'],
        link_dm=item['link_dm'],
        user=current_user
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


def get_didovi_items() -> list[ItemsForDed]:
    items = ItemFullData.select().where(ItemFullData.is_parsed == False)
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
#     s = get_didovi_items()
#     for i in s:
#         print(i)

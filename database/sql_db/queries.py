from peewee import IntegrityError
from schema.new_schema import ForGetProfileSchema, ItemsForDed
from .setup import db
from .tables import User, Item
from loguru import logger


def get_all() -> list[Item]:
    return Item.select(User)


def _save_user(profile_link: str, trade_link: str) -> User | None:
    try:
        if profile_link:
            with db.atomic():
                return User.create(profile=profile_link, trade_link=trade_link)
        return None
    except IntegrityError as err:
        logger.error(err)


def _save_item(item_name: str, dm_link: str, user: User = None):
    try:
        with db.atomic():
            Item.create(name=item_name, dm_link=dm_link, user=user)
    except IntegrityError as err:
        logger.error(err)


def save_item_in_db(item: ItemsForDed):
    current_user = _save_user(item['profile_link'], item['trade_link'])
    _save_item(
        item['name'], item['link_dm'], current_user
    )


# if __name__ == '__main__':
#     x = ItemsForDed(
#         link_dm='12345',
#         name='test',
#         profile_link='pr1of2',
#         trade_link='trade',
#         float_value=123.2,
#         paint_seed=2
#     )
#     save_item_in_db(x)

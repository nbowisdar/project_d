from loguru import logger

from csgofloat import auth, write_item
from database.sql_db.queries import save_item_in_db, get_didovi_items


@logger.catch
def did_part():
    # check auth
    bot = auth()

    items = get_didovi_items()
    for item in items:
        item = write_item(bot, item)

        try:
            save_item_in_db(item)
        except Exception as err:
            logger.error(err)
            logger.error(f"wrong item {item}")


if __name__ == '__main__':
    did_part()

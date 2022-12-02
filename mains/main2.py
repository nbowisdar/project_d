from loguru import logger

from csgofloat import auth, write_item
from database.sql_db.queries import save_item_in_db, get_didovi_items


@logger.catch
def did_part():
    # check auth
    auth()
    items = get_didovi_items()
    for item in items:
        logger.info(item)  # !!!!!!!!!!!!!!!!!!!!!!!!
        item = write_item(item)
        logger.info(item)  # !!!!!!!!!!!!!!!!!!!!!!!!!
        save_item_in_db(item)


if __name__ == '__main__':
    did_part()

from loguru import logger

from csgofloat import auth, write_item
from database.sql_db.queries import save_item_in_db, get_didovi_items


@logger.catch
def did_part():
    # check auth
    bot = auth()

    try:

        items = get_didovi_items()
        for item in items:
            item = write_item(bot, item)
            save_item_in_db(item)

    finally:
        bot.DRIVER.quit()


if __name__ == '__main__':
    did_part()

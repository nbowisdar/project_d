from database.sql_db.queries import check_new, save_only_items_in_db, get_didovi_items, get_sold_items
from database.sql_db.tables import create_table
from src.get_float_ import get_float
from src.get_items_dmarket import get_items_up_to_300
from loguru import logger
from telegram.messages import create_message, send_message

TELEGRAM_ID = 681903123

@logger.catch
def volodya_part():
    # create tables for db
    create_table()
    # max limit - 100
    #  get items from Dmarket
    items = get_items_up_to_300(price_up_to=7000, limit=30)
    # updated
    sold_items = get_sold_items(items)
    if sold_items:
        msg = create_message(sold_items)
        send_message(msg, TELEGRAM_ID)
    only_new = check_new(items)
    items_with_float = get_float(items=only_new, sec_sleep=0)
    logger.info(f'got new items - {len(items_with_float)}')
    save_only_items_in_db(items_with_float)


if __name__ == '__main__':
    volodya_part()
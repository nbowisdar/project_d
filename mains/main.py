from config import TELEGRAM_ID, PRICE_UP_TO, LIMIT, TIMEOUT, DELAY
from database.sql_db.queries import check_new, save_only_items_in_db, get_didovi_items, get_sold_items
from database.sql_db.tables import create_table
from schema.new_schema import ForGetFloatSchema
from src.get_float_ import get_float
from src.get_items_dmarket import get_items_up_to_300
from loguru import logger
from telegram.messages import create_message, send_message
import time


def get_items_form_dm(price_up_to: int, limit=100, show_msg=True) -> list[ForGetFloatSchema]:
    items = get_items_up_to_300(price_up_to, limit, show_msg)
    return items


def checking_sold_items(price_up_to: int, limit=100, timeout=0):
    while True:
        if timeout:
            time.sleep(timeout)
        print('checking sold items...')
        items = get_items_form_dm(price_up_to, limit, show_msg=False)
        sold_items = get_sold_items(items)
        if sold_items:
            msg = create_message(sold_items)
            send_message(msg, TELEGRAM_ID)


@logger.catch
def volodya_part():
    # create tables for db
    create_table()

    #  get items from Dmarket
    items = get_items_form_dm(price_up_to=PRICE_UP_TO, limit=LIMIT)
    only_new = check_new(items)

    items_with_float = get_float(items=only_new, delay=DELAY)
    logger.info(f'got new items - {len(items_with_float)}')
    save_only_items_in_db(items_with_float)


if __name__ == '__main__':
    while True:
        volodya_part()

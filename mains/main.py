from config import TELEGRAM_ID, PRICE_UP_TO, LIMIT, TIMEOUT, DELAY
from database.sql_db.queries import check_new, save_only_items_in_db, get_didovi_items, get_sold_items
from database.sql_db.tables import create_table
from schema.new_schema import ForGetFloatSchema
from src.get_float_ import get_float
from src.get_items_dmarket import get_items_up_to_300
from loguru import logger
from telegram.messages import create_message, send_message
import multiprocessing as ml
import time


def get_items_and_check_sold(price_up_to: int, limit=100, timeout=0) -> list[ForGetFloatSchema]:
    if timeout:
        time.sleep(timeout)
    print('checking sold items...')
    items = get_items_up_to_300(price_up_to, limit)
    # updated
    sold_items = get_sold_items(items)
    if sold_items:
        msg = create_message(sold_items)
        send_message(msg, TELEGRAM_ID)
    return items


@logger.catch
def volodya_part():
    # create tables for db
    create_table()

    #  get items from Dmarket
    items = get_items_and_check_sold(price_up_to=PRICE_UP_TO, limit=LIMIT, timeout=TIMEOUT)
    only_new = check_new(items)
    items_with_float = get_float(items=only_new, delay=DELAY)
    logger.info(f'got new items - {len(items_with_float)}')
    save_only_items_in_db(items_with_float)


# def volodya_part_upgraded():
#     main_proc = ml.Process(target=volodya_part)
#     telegram_proc = ml.Process(target=get_items_and_check_sold, args=(PRICE_UP_TO, LIMIT, TIMEOUT))
#     main_proc.start()
#     main_proc.join()
#     time.sleep(10)
#     print("start telegram bot")
#     telegram_proc.start()
#     telegram_proc.join()


if __name__ == '__main__':
    pass
    # volodya_part()
    # volodya_part_upgraded()

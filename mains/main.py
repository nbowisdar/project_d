from database.json_files.save_data import save_data
from database.sql_db.queries import check_new, save_only_items_in_db, get_didovi_items
from database.sql_db.tables import create_table
from src.get_float_ import get_float
from src.get_items_dmarket import get_items_up_to_300
from loguru import logger

@logger.catch
def volodya_part():
    # create tables for db
    create_table()
    items = get_items_up_to_300(7000)
    only_new = check_new(items)
    items_with_float = get_float(only_new)
    logger.info(f'got new items - {len(items_with_float)}')
    save_only_items_in_db(items_with_float)


# if __name__ == '__main__':
#     volodya_part()
#     s = get_didovi_items()
#     print(len(s))
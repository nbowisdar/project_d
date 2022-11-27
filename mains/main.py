from database.json_files.save_data import save_data
from database.sql_db.queries import check_new
from src.get_float_ import get_float
from src.get_items_dmarket import get_items_up_to_300


def volodya_part():
    items = get_items_up_to_300()
    only_new = check_new(items)
    items_with_float = get_float(only_new)
    save_data(items_with_float)


# if __name__ == '__main__':
#     volodya_part()
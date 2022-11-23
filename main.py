from database.json_files.save_data import save_data
from database.mongo_db.queries import DmMongo
from src.get_float_ import get_float
from src.get_items_dmarket import get_items_up_to_300



def main():
    items = get_items_up_to_300()
    # TODO check if we already have some items
    #only_new = check_new()
    items_with_float = get_float(items)
    save_data(items_with_float)


if __name__ == '__main__':
    main()
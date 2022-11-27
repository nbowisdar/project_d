from multiprocessing import freeze_support

from csgofloat import auth, write_item
from database.sql_db.queries import save_item_in_db
from database.json_files.save_data import get_items


def main():
    # need for freeze program
    freeze_support()
    # check auth
    auth()

    for item in get_items():
        item = write_item(item)
        save_item_in_db(item)


if __name__ == '__main__':
    main()

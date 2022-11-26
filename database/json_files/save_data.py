import json
from pathlib import Path

from schema.new_schema import ItemsForDed, ForGetProfileSchema


def save_data(data: list[ForGetProfileSchema]):
    with open('database/json_files/items_for_ded.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2)


def get_items() -> list[ItemsForDed]:
    # TODO вставь свой путь откуда будешь вызывать функцию
    # get path from execute file, if this 'items_for_ded.json' file will be in another folder this path dont work
    with open(Path(__file__).parent / 'items_for_ded.json', 'r', encoding='UTF-8') as file:
        for count, item in enumerate(json.load(file)):
            print(count)
            yield ItemsForDed(**item)


if __name__ == '__main__':
    from multiprocessing import freeze_support
    from csgofloat import auth, write_data

    # need for freeze program
    freeze_support()
    ############################ auth ##########################
    auth()

    ##################### work with your data ##################
    for item in get_items():
        write_data(item)

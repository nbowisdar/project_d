import json
from pathlib import Path

from schema.new_schema import ItemsForDed, ForGetProfileSchema, DedovResult


def save_data(data: list[ForGetProfileSchema]):
    with open('database/json_files/items_for_ded.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2)


def get_items() -> list[ItemsForDed]:
    # TODO вставь свой путь откуда будешь вызывать функцию
    with open(Path(__file__).parent / 'items_for_ded.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return [ItemsForDed(**item) for item in data]


# if __name__ == '__main__':
#     from multiprocessing import freeze_support
#     from csgofloat import main_csgofloat
#
#     freeze_support()
#     main_csgofloat()


    # def dedova_function(item: ItemsForDed) -> DedovResult:
    #     return DedovResult(profile_link='prof', trade_link='123')


    # items = get_items()
    # for item in items:
    #     profile_link, trade_link = dedova_function(item)
    #     item['profile_link'] = profile_link
    #     item['trade_link'] = trade_link

    # print(items[0])
    # TODO create function
    'save_data_to_db(items)'

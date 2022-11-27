import json
from schema.new_schema import ItemsForDed, ForGetProfileSchema
from csgofloat import path_near_exefile, wait_file_exists


def save_data(data: list[ForGetProfileSchema]):
    # simular '../../items_for_ded.json'
    with open(path_near_exefile().parent / 'items_for_ded.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2)


def get_items() -> list[ItemsForDed]:
    # wait file
    wait_file_exists(path_near_exefile().parent / 'items_for_ded.json')

    with open(path_near_exefile().parent / 'items_for_ded.json', 'r', encoding='UTF-8') as file:
        for item in json.load(file):
            yield ItemsForDed(**item)

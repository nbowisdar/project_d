import json
import os

from schema.new_schema import ItemsForDed, ForGetProfileSchema


def save_data(data: list[ForGetProfileSchema]):
    with open('database/json_files/items_for_ded.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)


def get_items() -> list[ItemsForDed]:
    # TODO вставь свой путь откуда будешь вызывать функцию
    with open('items_for_ded.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return [ItemsForDed(**item) for item in data]



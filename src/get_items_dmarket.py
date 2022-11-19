import json
import requests
from fake_useragent import UserAgent
from loguru import logger
from urls import build_dm_url, BASE_DM_ITEM_URL
from schema.items_schema import ForGetFloatSchema, ItemsSchema

UserAgent().random


def extract_in_game_and_link_dm(items: list) -> list[ForGetFloatSchema]:
    # for item in data['objects']:
    rez = []
    for item in items:
        rez.append(ForGetFloatSchema(
            link_dm=BASE_DM_ITEM_URL + item['extra']['linkId'],
            in_game=item['extra']['inspectInGame']
        ))
    return rez


def get_one_page(url: str) -> dict:
    headers = {'User-Agent': UserAgent().random}
    with requests.Session() as session:
        with session.get(url, headers=headers) as resp:
            return resp.json()


# grab all items from dm up to 300$
def main():
    rez = []
    price_from = 0

    while price_from < 30000:
        current_url = build_dm_url(price_from)
        data = get_one_page(current_url)
        items = data['objects']
        rez.extend(extract_in_game_and_link_dm(items))
        price = int(items[-1]['price']['USD'])

        logger.info(f'max price - {price/100}$')
        price_from = price

    d = ItemsSchema(items=rez)
    with open('output/items.json', 'w', encoding='utf8') as file:
        json.dump(d.dict(), file, indent=2)


if __name__ == '__main__':
    main()






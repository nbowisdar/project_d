import time

import requests
from src.fake_agents import FakeAgent
from loguru import logger
from src.urls import build_dm_url, BASE_DM_ITEM_URL
from schema.new_schema import ForGetFloatSchema

agent = FakeAgent()


def extract_in_game_and_link_dm(items: list) -> list[ForGetFloatSchema]:
    # for item in data['objects']:
    rez = []
    for item in items:
        rez.append(ForGetFloatSchema(
            item_name=item["title"],
            # item_name=item['extra']['name'],
            link_dm=BASE_DM_ITEM_URL + item['extra']['linkId'],
            in_game=item['extra']['inspectInGame']
        ))

    return rez


def get_one_page(url: str) -> dict:
    headers = {'User-Agent': agent.random()}
    with requests.Session() as session:
        with session.get(url, headers=headers) as resp:
            return resp.json()


# grab all items from dm up to 300$
def get_items_up_to_300(price_up_to=30000, limit=100, show_msg=True, delay=0) -> list[ForGetFloatSchema]:
    rez = []
    price_from = 0

    while price_from < price_up_to:
        current_url = build_dm_url(price_from=price_from, limit=limit)
        try:
            if delay:
                time.sleep(delay)
            data = get_one_page(current_url)
        except RuntimeError:
            logger.error("Server doesn't respond")
            print("Try again...")
            continue
        items = data['objects']
        rez.extend(extract_in_game_and_link_dm(items))
        price = int(items[-1]['price']['USD'])

        print(f'Getting from dm... {price/(price_up_to / 100)} / 100%')
        price_from = price

    if show_msg:
        logger.info(f'Got {len(rez)} new items from dm!')
    return rez



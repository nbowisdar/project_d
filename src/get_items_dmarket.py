from fake_useragent import UserAgent
import requests
import json
from schema.items_schema import ForGetFloatSchema

UserAgent().random


def get_all_items_from_dm() -> dict:
    headers = {'User-Agent': UserAgent().random}
    # TODO: I can get only 100 items, but I can change price FROM and TO, so I wll send many request with diff param.
    url = 'https://api.dmarket.com/exchange/v1/market/items?' \
          'side=market&' \
          'orderBy=personal&' \
          'orderDir=desc&' \
          'title=knife&' \
          'priceFrom=0&' \
          'priceTo=30000&' \
          'treeFilters=&gameId=a8db&' \
          'types=p2p&' \
          'cursor=WzMxMDIsMTY2NTE1ODk5OTAwMCwiOWE2YzU4Y2EtYmFkMi00MWM5LTk0YTctMzBkNzFlNmM5ZDIzIl0=&' \
          'limit=100&' \
          'currency=USD&platform=browser&isLoggedIn=true'
    return requests.get(url, headers=headers).json()


BASE_ITEM_URL = 'https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId='


def get_in_game_and_link_dm(items: list) -> list[ForGetFloatSchema]:
    # for item in data['objects']:
    rez = []
    for item in items:
        rez.append(ForGetFloatSchema(
            link_dm=BASE_ITEM_URL + item['extra']['linkId'],
            in_game=item['extra']['inspectInGame']
        ))
    return rez



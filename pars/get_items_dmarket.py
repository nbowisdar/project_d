from fake_useragent import UserAgent
import requests

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
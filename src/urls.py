def build_dm_url(*, price_from: int, price_to=40000, what='knife', limit=100):
    return 'https://api.dmarket.com/exchange/v1/market/items' \
           '?side=market&orderBy=price&orderDir=asc&' \
           f'title={what}&priceFrom={price_from}&priceTo={price_to}&treeFilters=&gameId=a8db&types=p2p' \
           '&cursor=WzAuMDIsIjE0ODk0OWM5LTMxN2MtNDljOC05YTk2LWU3M2Q5OTdjYjVmOCJd' \
           f'&limit={limit}&currency=USD&platform=browser&isLoggedIn=true'


BASE_DM_ITEM_URL = 'https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId='
BASE_FLOAT_URL = 'https://api.csgofloat.com/?url='

from loguru import logger

from .works_fs import path_near_exefile  # if you need path to your file
from .api_csgofloat import CSGOfloatApi


@logger.catch
def auth():

    with CSGOfloatApi(user_data_dir=path_near_exefile("Profile") / "User Data") as api:
        api.auth_csgofloat()

        return api


@logger.catch
def write_item(api, item):
    url_account, trade_link = api.get_links(item)
    item['profile_link'] = url_account
    item['trade_link'] = trade_link

    return item

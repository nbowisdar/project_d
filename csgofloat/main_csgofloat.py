from .works_fs import path_near_exefile  # if you need path to your file
from .interface import get_profile
from .api_csgofloat import CSGOfloatApi


def auth():

    global api

    api = CSGOfloatApi(user_data_dir=path_near_exefile("Profiles") / get_profile()[0] / "User Data")
    api.auth_csgofloat()


def write_data(item):
    url_account, trade_link = api.get_links(item)
    print(url_account)
    print(trade_link)
    item['profile_link'] = url_account
    item['trade_link'] = trade_link

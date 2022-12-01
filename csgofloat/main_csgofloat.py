from .works_fs import path_near_exefile  # if you need path to your file
from .api_csgofloat import CSGOfloatApi


def auth():
    global api

    api = CSGOfloatApi(user_data_dir=path_near_exefile("Profile") / "User Data")
    try:
        api.auth_csgofloat()
    finally:
        api.DRIVER.quit()


def write_item(item):
    try:
        url_account, trade_link = api.get_links(item)
        item['profile_link'] = url_account
        item['trade_link'] = trade_link
    finally:
        api.DRIVER.quit()

    return item

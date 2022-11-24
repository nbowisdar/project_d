from .works_fs import path_near_exefile  # if you need path to your file
from .interface import get_profile
from .api_csgofloat import CSGOfloatApi


def auth():
    global api
    api = CSGOfloatApi(user_data_dir=path_near_exefile("Profiles") / get_profile()[0] / "User Data")
    api.auth_csgofloat()


def write_data(item):
    api.get_links(item)
    # item['profile_link'] = profile_link
    # item['trade_link'] = trade_link

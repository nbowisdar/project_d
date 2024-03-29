from loguru import logger

from database.sql_db.queries import save_item_in_db, get_didovi_items

from csgofloat import path_near_exefile  # if you need path to your file
from csgofloat import CSGOfloatApi


@logger.catch
def did_part():
    # check auth
    with CSGOfloatApi(user_data_dir=path_near_exefile("Profile") / "User Data") as api:
        api.auth_csgofloat()  # Log in the csgofloat via steam
        items = get_didovi_items()  # Vova's part
        for item in items:
            url_account, trade_link = api.get_links(item)  # get steam account and trade link

            # save items in the dict
            item['profile_link'] = url_account
            item['trade_link'] = trade_link

            try:
                save_item_in_db(item)  # Vova's part
            except Exception as err:
                logger.error(err)
                logger.error(f"wrong item {item}")


if __name__ == '__main__':
    did_part()

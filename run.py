import time
from threading import Thread
from multiprocessing import freeze_support
from loguru import logger

from database.sql_db.tables import create_table
from telegram import start_tg_bot
from csgofloat import check_profile_exists
from config import TELEGRAM_ID, PRICE_UP_TO, LIMIT, TIMEOUT

from mains.main import volodya_part, get_items_form_dm, checking_sold_items
from mains.main2 import did_part
from telegram.messages import send_messages


@logger.catch
def main(iteration_counter: int):
    # for work chrome through profile
    #check_profile_exists()

    # first part
    volodya_part()

    # second part
    #did_part()
    logger.info(f"Iteration finished successfully №-{iteration_counter}")


if __name__ == '__main__':
    #freeze_support()
    create_table()
    send_messages("Бот запущен!", TELEGRAM_ID)

    # need for freeze program
    try:
        logger.add(
            "csgo.log",
            format="{time} {level} {message}",
            level="ERROR",
            rotation="10 MB",
            compression="zip"
        )

        # run tg bot
        bot_proc = Thread(target=start_tg_bot)
        pars_sold_proc = Thread(target=checking_sold_items, args=(PRICE_UP_TO, LIMIT, TIMEOUT))
        bot_proc.start()
        pars_sold_proc.start()
        count = 0
        while True:
            main(count)
            count += 1
            time.sleep(30)

    finally:
        input()

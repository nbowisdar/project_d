import time
from threading import Thread
from multiprocessing import freeze_support
from loguru import logger

from telegram import start_tg_bot
from csgofloat import check_profile_exists
from config import TELEGRAM_ID, PRICE_UP_TO, LIMIT, TIMEOUT

from mains.main import volodya_part, get_items_and_check_sold, checking_sold_items
from mains.main2 import did_part


@logger.catch
def main(iteration_counter: int):
    # for work chrome through profile
    check_profile_exists()

    # first part
    volodya_part()

    # second part
    did_part()
    logger.info(f"Iteration finished successfully №-{iteration_counter}")


if __name__ == '__main__':
    freeze_support()

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
        logger.info('Telegram bot start runing')

        while True:
            count = 0
            logger.info("Start new iteration")
            main(count)
            count += 1
            print("Well done, went through all items! Start new iteration...")

    finally:
        input()

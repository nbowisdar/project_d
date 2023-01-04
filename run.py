from multiprocessing import freeze_support, Process
from loguru import logger
from mains.main import volodya_part, get_items_and_check_sold
from mains.main2 import did_part
from telegram import start_tg_bot
from csgofloat import check_profile_exists
from config import TELEGRAM_ID, PRICE_UP_TO, LIMIT, TIMEOUT


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

    # need for freeze program
    try:
        freeze_support()

        logger.add(
            "csgo.log",
            format="{time} {level} {message}",
            level="ERROR",
            rotation="10 MB",
            compression="zip"
        )

        # run tg bot
        bot_proc = Process(target=start_tg_bot)
        pars_sold_proc = Process(target=get_items_and_check_sold, args=(PRICE_UP_TO, LIMIT, TIMEOUT))
        bot_proc.start()
        pars_sold_proc.start()
        logger.info('Telegram bot start runing')

        while True:
            count = 0
            logger.info("Start new iteration")
            main(count)
            count += 1
            break

    finally:
        input()

from multiprocessing import freeze_support
from loguru import logger
from mains.main import volodya_part
from mains.main2 import did_part
from telegram import start_tg_bot
from csgofloat import check_profile_exists


@logger.catch
def main():
    # for work chrome through profile
    check_profile_exists()
    # start telegram bot
    start_tg_bot()
    # first part
    volodya_part()


    # second part
    did_part()


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

        main()

    finally:
        input()

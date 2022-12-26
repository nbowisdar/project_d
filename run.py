from multiprocessing import freeze_support, Process
from loguru import logger
from mains.main import volodya_part
from mains.main2 import did_part
from telegram import start_tg_bot
from csgofloat import check_profile_exists


@logger.catch
def main():
    # for work chrome through profile
    check_profile_exists()

    # run tg bot
    bot_proc = Process(target=start_tg_bot)
    bot_proc.start()
    logger.info('Telegram bot start runing')
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

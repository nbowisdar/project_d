from multiprocessing import freeze_support
from loguru import logger

from mains.main import volodya_part
from mains.main2 import did_part

from csgofloat import check_profile_exists

@logger.catch
def main():
    # for work chrome through profile
    check_profile_exists()

    # first part
    try:
        volodya_part()
    except Exception as err:
        logger.error(err)
        logger.error('Volodya made a mistake')

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

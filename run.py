from mains.main import volodya_part
from mains.main2 import did_part
from loguru import logger


def main():
    # first part
    try:
        volodya_part()
    except Exception as err:
        logger.error(err)
        logger.error('Volodya made a mistake')

    # second part
    try:
        did_part()
    except Exception as err:
        logger.error(err)
        logger.error('Did made a mistake')


if __name__ == '__main__':
    main()

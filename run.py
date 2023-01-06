from multiprocessing import freeze_support, Process
from loguru import logger
from mains.main import volodya_part, get_items_and_check_sold
from mains.main2 import did_part
from telegram import start_tg_bot
from csgofloat import check_profile_exists
from config import TELEGRAM_ID, PRICE_UP_TO, LIMIT, TIMEOUT
import os
import sys

try:
    if sys.platform.startswith('win'):
        from multiprocessing.popen_spawn_win32 import Popen

    else:
        from multiprocessing.popen_fork import Popen

except ImportError:
    pass


# First define a modified version of Popen.
class _Popen(Popen):
    def __init__(self, *args, **kw):

        if hasattr(sys, 'frozen'):
            # We have to set original _MEIPASS2 value from sys._MEIPASS
            # to get --onefile mode working.
            os.putenv('_MEIPASS2', sys.executable)
        try:
            super(_Popen, self).__init__(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                # available. In those cases we cannot delete the variable
                # but only set it to the empty string. The bootloader
                # can handle this case.
                if hasattr(os, 'unsetenv'):
                    os.unsetenv('_MEIPASS2')
                else:
                    os.putenv('_MEIPASS2', '')


@logger.catch
def main(iteration_counter: int):
    # for work chrome through profile
    check_profile_exists()

    # first part
    volodya_part()

    # second part
    # did_part()
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

        if sys.platform.startswith('win'):
            # Second override 'Popen' class with our modified version.
            Popen = _Popen

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

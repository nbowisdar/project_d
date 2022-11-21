import os
import random
import time
import datetime

from loguru import logger
from pathlib import Path
from multiprocessing import freeze_support

import handling_file_system as work_fs
from interface import get_profile
from api_csgofloat import CSGOfloatApi


@logger.catch
def main():
    profile = get_profile()

    # while True:
    #     start_time = time.perf_counter()

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Началась сессия загрузки.")
    api = None

    try:
        api = CSGOfloatApi(user_data_dir=work_fs.path_near_exefile("Profiles") / profile / "User Data")
    finally:
        api.DRIVER.quit()

        # time_end_execution = time.perf_counter() - start_time
        # random_sleep = random.uniform(6300, 8100)

        # if time_end_execution < random_sleep:
        #     pause = random_sleep - time_end_execution
        #     time.sleep(pause)

#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Default"
if __name__ == '__main__':
    freeze_support()
    logger.add("error.log", format="{time} {level} {message}", level="ERROR", rotation="1 month", compression="zip")
    main()

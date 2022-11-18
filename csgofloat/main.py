import os
import random
import time
import datetime

from loguru import logger
from pathlib import Path
from multiprocessing import freeze_support

import handling_file_system as work_fs
from upload_tiktok import ApiTikTok
from video_edit import VideoEdit
from interface import interface


def video_edit() -> str:
    path_to_video = str(sorted(work_fs.path_near_exefile().glob("*.mp4"))[0])
    path_to_downloads = Path(rf"{os.environ['USERPROFILE']}/Downloads/")

    ve = VideoEdit()
    ve.attend_page()

    name_video = path_to_video.split("\\")[-1]

    ve.video_processing(path_to_video)

    zipfile_path = path_to_downloads / ve.name_download_file
    work_fs.wait_download(zipfile_path)

    ve.DRIVER.quit()

    work_fs.unziping(path_to_zipfile=zipfile_path,
                     unzip_path=work_fs.path_near_exefile('video') / name_video
                     )

    return name_video


def uploader(profiles):
    for profile in profiles:
        api = False
        try:
            api = ApiTikTok(user_data_dir=work_fs.path_near_exefile("Profiles") / profile / "User Data")
            path_video = work_fs.auto_create("video", _type="dir") / video_edit()
            api.upload_video(path_video, work_fs.getter_file_list("Tags.txt"))

            # delete video after session
            path_video.unlink()
        finally:
            api.DRIVER.quit()


@logger.catch
def main():
    profiles = interface()

    while True:
        start_time = time.perf_counter()
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Началась сессия загрузки.")
        uploader(profiles)

        time_end_execution = time.perf_counter() - start_time
        random_sleep = random.uniform(6300, 8100)

        if time_end_execution < random_sleep:
            pause = random_sleep - time_end_execution
            time.sleep(pause)

#
# if __name__ == '__main__':
#     freeze_support()
#     logger.add("error.log", format="{time} {level} {message}", level="ERROR", rotation="1 month", compression="zip")
#     main()

import os
import shutil

from subprocess import call
from colorama import init, deinit

import handling_file_system as work_fs


def call_cmd_profile(new_path_profile):
    if work_fs.file_exists(r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        path_to_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    else:
        path_to_chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    path_profile = f"{new_path_profile}"  # User Data
    command = f'"{path_to_chrome}" --user-data-dir="{path_profile}"'
    call(command)

    return get_profile()


def delete_chrome_profile(new_path_profile):
    for profile in new_path_profile.glob("Profile*"):  # search in copy User Data
        shutil.rmtree(profile, ignore_errors=True)

    return call_cmd_profile(new_path_profile)


def copy_chrome_folder():
    """find and copy your default"""
    absolute_path_profiles = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
    new_path_profile = work_fs.path_near_exefile("Profiles") / "Profile" / "User Data"

    shutil.copytree(absolute_path_profiles, new_path_profile)

    return delete_chrome_profile(new_path_profile)


def get_profile():
    list_profiles = os.listdir(work_fs.auto_create(f"Profiles", "dir"))
    init()
    if list_profiles:
        deinit()
        return list_profiles

    else:
        work_fs.warning_text("Нет профилей")
        print("Дождись запуска браузера!")
        return copy_chrome_folder()

import os
import shutil

from subprocess import call
from colorama import init, deinit

import undetected_chromedriver as uc
from .works_fs import path_near_exefile, auto_create, warning_text, magenta_color, green_color


def call_cmd_profile(new_path_profile):
    path_to_chrome = uc.find_chrome_executable()

    path_profile = f"{new_path_profile}"  # User Data
    command = f'"{path_to_chrome}" --user-data-dir="{path_profile}"'

    print(green_color('Создай профиль и авторизуйся через "Steam" в "CSGOfloat".'))
    input("Are you ready? Press Enter: ")
    call(command)

    return check_profile_exists()


def delete_chrome_profile(new_path_profile):
    for profile in new_path_profile.glob("Profile*"):  # search in copy User Data
        shutil.rmtree(profile, ignore_errors=True)

    return call_cmd_profile(new_path_profile)


def copy_chrome_folder():
    """find and copy your default"""
    absolute_path_profiles = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
    new_path_profile = path_near_exefile("Profile") / "User Data"

    shutil.copytree(absolute_path_profiles, new_path_profile)

    return delete_chrome_profile(new_path_profile)


def check_profile_exists():
    list_profiles = os.listdir(auto_create(path_near_exefile("Profile"), "dir"))

    init()
    if list_profiles:
        deinit()
        return

    else:
        warning_text('Нет профиля. Создайте профиль и войдите в "csgofloat" через Steam')
        print(magenta_color("Дождись запуска браузера!"))
        return copy_chrome_folder()

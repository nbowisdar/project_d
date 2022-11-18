import glob
import os
import shutil

from subprocess import call

from colorama import init, deinit

import handling_file_system as work_fs

yes = ["y", "yes", '']
no = ["n", "no"]


def data_confirmation(massage) -> bool:
    print(work_fs.blue_color(massage + work_fs.green_color("?[Y/n]")))
    answer = input().replace(" ", "").lower()
    if answer in yes:
        return True

    elif answer in no:
        return False

    else:
        print(f"Выбери yes or no")
        return data_confirmation(massage)


def call_cmd_profile(new_path_profile):
    if work_fs.file_exists(r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        path_to_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    else:
        path_to_chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    path_profile = f"{new_path_profile}"  # User Data
    command = f'"{path_to_chrome}" --user-data-dir="{path_profile}"'
    call(command)


def delete_chrome_profile(new_path_profile):

    for profile in new_path_profile.glob("Profile*"): # search in copy User Data
        shutil.rmtree(profile, ignore_errors=True)

    return call_cmd_profile(new_path_profile)


def copy_chrome_folder():
    """find and copy your default"""
    absolute_path_profiles = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
    print(work_fs.blue_color("Tiktok аккаунт: "))
    email = str(input())
    new_path_profile = work_fs.path_near_exefile("Profiles") / email / "User Data"

    try:
        shutil.copytree(absolute_path_profiles, new_path_profile)
    except FileExistsError:
        work_fs.warning_text(f"Такой гугл аккаунт уже есть{new_path_profile}")
        return

    return delete_chrome_profile(new_path_profile)


def create_profile():
    count = 0
    while True:
        work_fs.warning_text("Важно вход вручную. Нужно войти вручную в тикток и гугл.")
        try:
            print(work_fs.blue_color("Сколько нужно профилей?: "))
            count = int(input())
            break
        except ValueError:
            work_fs.warning_text("Введи целое число")
            continue

    for _ in range(count):
        copy_chrome_folder()


def interface():
    list_profiles = os.listdir(work_fs.auto_create(f"Profiles", "dir"))

    init()
    print(f"""Начать работу программы нажмите{work_fs.green_color('"Enter"')}.""")
    print(f'Добавить профиль {work_fs.yellow_color("add")}')

    print(work_fs.blue_color("Что делаем? "))
    answer = input("").lower().replace(" ", "").replace("\n", "")

    if answer:
        if answer == "add":
            create_profile()

        else:
            work_fs.warning_text("Не понятно что делать.")

        return interface()

    deinit()

    if list_profiles:
        return list_profiles
    else:
        work_fs.warning_text("Нет профилей")

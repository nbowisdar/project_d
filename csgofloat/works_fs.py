import ctypes
import os
import sys
import time

from pathlib import Path
import subprocess
import random
from colorama import Fore, Style, Back


def warning_text(text):
    print(Fore.RED + "warning! -> " + Style.RESET_ALL + Back.RED + Fore.WHITE + str(text) + Style.RESET_ALL)


def blue_color(text):
    return Fore.LIGHTBLUE_EX + str(text) + Style.RESET_ALL


def green_color(text):
    return Fore.GREEN + str(text) + Style.RESET_ALL


def cyan_color(text):
    return Fore.LIGHTCYAN_EX + str(text) + Style.RESET_ALL


def yellow_color(text):
    return Fore.YELLOW + str(text) + Style.RESET_ALL


def magenta_color(text):
    return Fore.LIGHTMAGENTA_EX + str(text) + Style.RESET_ALL


def file_exists(path_to_file) -> bool:
    """Check file exists by path"""
    path = Path(path_to_file)

    if path.is_file():
        return True
    else:
        return False


def dir_exists(path_to_dir) -> bool:
    """Check directory exists by path"""
    path = Path(path_to_dir)

    if path.is_dir():
        return True
    else:
        return False


def path_near_exefile(filename=""):
    """
    create=visible :create folder or file is visible for users
    create=hidden :create folder or file is hidden for users

    return path to file near executable file
    """

    if getattr(sys, 'frozen', False):
        path = Path(sys.executable).parent / filename

    else:
        path = Path(__file__).parent / filename

    return path


def auto_create(filename, _type, hidden=False):
    """
    _type=file
    _type=dir
    """
    path = path_near_exefile(filename)

    if _type == "file":

        if not file_exists(path):
            # is not exists, program creates
            # if create == "visible":
            #     open(path_near_exefile(filename), "w", encoding="utf8", errors="ignore").close()
            open(path_near_exefile(filename), "a", encoding="utf8", errors="ignore").close()

            if hidden:
                subprocess.call("attrib +h " + str(path))

    elif _type == "dir":
        if not dir_exists(path):
            # if create == "visible":
            os.makedirs(path)

            if hidden:
                subprocess.call("attrib +h " + str(path))

    else:
        raise Exception(f"Invalid flag _type='{_type}'")

    return path


def getter_file_list(filename) -> list:
    """
    Get list from file by path.
    """

    with open(path_near_exefile(filename), "r", encoding="utf8", errors='ignore') as file:
        list_from_file = [line.strip() for line in file.readlines() if line != "\n"]
        list_from_file.sort()

    return list_from_file


def write_line(filename, list_line):
    """Writes line in file. Rewrite all info in the file."""
    with open(path_near_exefile(filename), "w+", encoding="utf8", errors="ignore") as file:

        if isinstance(list_line, list):
            list_line = [line for line in list_line if line.strip()]
            list_line.sort()

            file.seek(0)
            file.truncate()
            file.write("\n".join(str(line) for line in list_line))

        elif isinstance(list_line, str):
            file.seek(0)
            file.truncate()
            file.write(list_line + "\n")


# def add_list_file(filename, info_as_list):
#     """
#     info_as_list - this foo information which need to write in the file
#     """
#
#     list_line = *getter_file_list(filename), *info_as_list
#     write_line(filename, list_line)
# with open(path_near_exefile(filename), "r+", encoding="utf8") as writer:
#     for line in info:
#         if line.strip():
#             print(line)
#             writer.write("\n".join(str(line)))
#     writer.truncate()


def adder_list(filename, list_line):
    with open(path_near_exefile(filename), "a+", encoding="utf8", errors="ignore") as file:
        if list_line:
            if isinstance(list_line, list):
                list_line = [line for line in list_line if line.strip()]
                list_line.sort()

                file.writelines(list_line)

            elif isinstance(list_line, str):
                file.write(list_line)


def delete_line(filename, number=str):
    """delete information by index from file"""
    with open(path_near_exefile(filename), "a+", encoding="utf8", errors="ignore") as file:
        lines = file.readlines()
        lines.sort()

        # del lines[index]
        for line in lines:
            if line.strip(":")[0] == number:
                del lines[lines.index(line)]

        lines = [line for line in lines if line.strip()]

        file.seek(0)
        file.truncate()
        file.writelines(lines)


def wait_file_exists(filepath):
    while not file_exists(filepath):
        time.sleep(1)

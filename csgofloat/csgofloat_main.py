
import csgofloat.works_fs as work_fs
from .interface import get_profile
from api_csgofloat import CSGOfloatApi


def main_csgofloat():
    profile = get_profile()
    api = None

    try:
        api = CSGOfloatApi(user_data_dir=work_fs.path_near_exefile("Profiles") / profile / "User Data")
    finally:
        api.DRIVER.quit()


# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Default"
# TODO авторизоваться
from src.get_float_ import pars_all, start_parsing
from src.get_items_dmarket import get_all_items_from_dm, get_in_game_and_link_dm


def main():
    items = get_all_items_from_dm()
    # TODO check if we already have some items
    only_new = check_new()
    in_game_and_link = get_in_game_and_link_dm(items['objects'])
    start_parsing(in_game_and_link, save=True)

main()

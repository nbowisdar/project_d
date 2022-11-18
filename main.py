from requests import get
import json

BASE_ITEM_URL = 'https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId='

with open('file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data['objects']:
    in_game = item['extra']['inspectInGame']
    item_link = BASE_ITEM_URL + item['extra']['linkId']

    #print(item_link)
    print(in_game)

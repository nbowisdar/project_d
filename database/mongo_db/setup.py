import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.steam
dm_items = db.dm_items


# if __name__ == '__main__':
#     item = {'name': 'Aka-47', 'price': 300}
#     dm_items.insert_one(item)

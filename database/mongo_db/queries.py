from pprint import pprint
from database.mongo_db.setup import dm_items
from loguru import logger

from schema.new_schema import ItemsForDed


class DmMongo:
    def __init__(self):
        self.collection = dm_items

    def save_all(self, items: list[dict]):
        self.collection.insert_many(items)
        logger.info('Saved new date!')


    def get_items(self) -> list[ItemsForDed]:
        query = self.collection.find()
        return [ItemsForDed(**item) for item in query]

    def drop_all(self) -> bool:
        self.collection.delete_many({})
        return True

    def delete_prev_save_new(self, items: list[dict]):
        self.drop_all()
        self.save_all(items)

#
if __name__ == '__main__':
    dm = DmMongo()
    items = dm.get_items()
    for i in items:
        print(i['name'])


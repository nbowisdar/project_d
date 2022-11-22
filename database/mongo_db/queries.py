from pprint import pprint
from database.mongo_db.setup import dm_items
from loguru import logger

class DmMongo:
    def __init__(self):
        self.collection = dm_items

    def save_all(self, items: list[dict]):
        self.collection.insert_many(items)
        logger.info('Saved new date!')

    def get_items(self) -> list[dict]:
        query = self.collection.find()
        return [item for item in query]

    def drop_all(self) -> bool:
        self.collection.delete_many({})
        return True

    def delete_prev_save_new(self, items: list[dict]):
        self.drop_all()
        self.save_all(items)

#
# if __name__ == '__main__':
#     dm = DmMongo()
#     items = [{'name': 'test', 'price': 210},
#              {'name': 'twodwad', 'price': 340}]
#     dm.delete_prev_save_new(items)
#     s = dm.get_items()
#     print(s)


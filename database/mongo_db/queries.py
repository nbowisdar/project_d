from pprint import pprint
from database.mongo_db.setup import dm_items
from loguru import logger

from schema.items_schema import ForGetProfileSchema


class DmMongo:
    def __init__(self):
        self.collection = dm_items

    def save_all(self, items: list[dict]):
        self.collection.insert_many(items)
        logger.info('Saved new date!')

    def get_items(self) -> list[ForGetProfileSchema]:
        query = self.collection.find()
        rez = []
        for i in query:
            rez.append(ForGetProfileSchema(
                name=i['name'],
                link_dm=i['link_dm'],
                float_value=i['float_value'],
                paint_seed=i['paint_seed']
            ))
        return rez

    def drop_all(self) -> bool:
        self.collection.delete_many({})
        return True

    def delete_prev_save_new(self, items: list[dict]):
        self.drop_all()
        self.save_all(items)

#
# if __name__ == '__main__':
#     dm = DmMongo()
#     items = dm.get_items()
#     for item in items:
#         print(item)



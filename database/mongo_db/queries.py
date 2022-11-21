from setup import db


class MongoData:
    def __init__(self):
        self.db = db

    def def_all(self) -> list:
        pass

    def save_new_data(self, data: list):
        pass

    def prune_table(self):
        pass
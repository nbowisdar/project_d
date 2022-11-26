from database.sql_db.setup import db, BaseModel
from peewee import Model, CharField, ForeignKeyField


class User(BaseModel):
    #name = CharField()
    profile = CharField(unique=True)
    trade_link = CharField(null=True)


class Item(BaseModel):
    name = CharField()
    dm_link = CharField(unique=True)
    user = ForeignKeyField(User, backref='items', null=True)


if __name__ == '__main__':
    with db.atomic():
        db.create_tables([User, Item])
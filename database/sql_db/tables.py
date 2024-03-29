from database.sql_db.setup import db, BaseModel
from peewee import Model, CharField, ForeignKeyField, IntegerField, FloatField, BooleanField
import os
int(os.environ.get("PORT", 5000))


class User(BaseModel):
    # name = CharField()
    profile = CharField(unique=True, null=True)
    trade_link = CharField(null=True)


class Item(BaseModel):
    name = CharField()
    link_dm = CharField(unique=True)
    # float_value = FloatField()
    # paint_seed = IntegerField()
    user = ForeignKeyField(User, backref='items', null=True)


class ItemFullData(BaseModel):
    link_dm = CharField()
    name = CharField()
    float_value = FloatField()
    paint_seed = IntegerField()
    is_parsed = BooleanField(default=False)


def create_table():
    with db.atomic():
        db.create_tables([User, Item, ItemFullData])


if __name__ == '__main__':
    create_table()

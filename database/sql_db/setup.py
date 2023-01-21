from peewee import SqliteDatabase, Model
from csgofloat import path_near_exefile

db = SqliteDatabase(path_near_exefile('app.db'))


class BaseModel(Model):
    class Meta:
        database = db
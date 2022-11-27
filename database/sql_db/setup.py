from peewee import SqliteDatabase, Model
from csgofloat import path_near_exefile

db = SqliteDatabase(path_near_exefile().parent / 'app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class BaseModel(Model):
    class Meta:
        database = db
from peewee import SqliteDatabase, Model

db = SqliteDatabase('app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class BaseModel(Model):
    class Meta:
        database = db
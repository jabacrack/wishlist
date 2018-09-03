from peewee import *
from playhouse.sqlite_ext import  AutoIncrementField, SqliteExtDatabase

database_file = "data.sqlite"
db = SqliteExtDatabase(database_file, pragmas=(('foreign_keys', 'on'),) )

class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    id = AutoIncrementField()
    name = TextField()
    login = TextField()
    password = TextField()

class WishList(BaseModel):
    # user = ForeignKeyField(User, related_name='wishlist')
    name = TextField()
    description = TextField(null=True)
    cost = TextField(null=True)
    links = TextField(null=True)
    picture = TextField(null=True)

db.create_table(User, safe=True)
db.create_table(WishList, safe=True)

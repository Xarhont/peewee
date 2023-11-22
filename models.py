from peewee import *

db = SqliteDatabase('test.db')


class Base(Model):
    class Meta:
        database = db

class Kl_ruk(Base):
    name = CharField()

class Klass(Base):
    name = CharField()
    ruk = ForeignKeyField(Kl_ruk, backref='Klasses')

class Student(Base):
    name = CharField()
    klass = ForeignKeyField(Klass, backref='students')

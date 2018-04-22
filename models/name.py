from mongoengine import *


class User(Document):
    fullname = StringField()
    email = StringField()
    username = StringField(unique=True)
    password = StringField()


class Name(Document):
    name = StringField()
    audio = StringField()

class Character(Document):
    char = StringField()
    audio = StringField()

class State(Document):
    state = StringField()
    audio = StringField()

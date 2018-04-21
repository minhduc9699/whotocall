from mongoengine import *

class Name(Document):
    name = StringField(unique=True, required=True)
    audio = StringField(unique=True)

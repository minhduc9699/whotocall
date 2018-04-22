from mongoengine import *

class Name(Document):
    name = StringField(required=True)
    audio = StringField(required=True)

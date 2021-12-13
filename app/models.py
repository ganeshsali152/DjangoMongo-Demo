from django.db import models
from mongoengine import Document, fields


class Movie(Document):
    title = fields.StringField(required=True)
    year = fields.IntField()
    rated = fields.StringField()


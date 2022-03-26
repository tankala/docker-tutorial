from enum import unique
from app import db

class Book(db.Model):
    title = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    pwd = db.Column(db.String(80))

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, uid):
        return cls.query.filter_by(id=uid).first()


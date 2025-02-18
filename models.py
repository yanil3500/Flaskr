# cSpell: ignore flaskr
from app import db


class Flaskr(db.Model):
    __tablename__ = 'flaskr'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, primary_key=False)
    text = db.Column(db.String, primary_key=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<title {}>'.format(self.body)

from app import db

class Deck(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    processed = db.Column(db.Integer, default=0, nullable=False)
    datetime_uploaded = db.Column(db.DateTime, nullable=False)
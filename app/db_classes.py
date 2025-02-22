from app import db

class Deck(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    
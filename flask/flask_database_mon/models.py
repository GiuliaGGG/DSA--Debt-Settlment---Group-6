from flask_app import db


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(100), nullable=False)
    paypal_username = db.Column(db.String(100))


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float, nullable=False)

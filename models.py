from flask import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(120))
    gender = db.Column(db.String(10))
    identification_type = db.Column(db.String(20))
    national_id = db.Column(db.String(20))
    passport = db.Column(db.String(20))

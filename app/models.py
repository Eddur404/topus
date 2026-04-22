from db import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(70), unique=True)
    nome = db.Column(db.String(40))
    senha = db.Column(db.String())
# account.py

from hashlib import sha256
from db import db  # Assuming db is the Flask SQLAlchemy instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

def create_database():
    db.create_all()

def add_user(username, password):
    hashed_password = sha256(password.encode()).hexdigest()
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

def authenticate_user(username, password):
    hashed_password = sha256(password.encode()).hexdigest()
    user = User.query.filter_by(username=username, password=hashed_password).first()
    return user is not None

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

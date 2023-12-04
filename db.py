from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request

# For more information about database configuration checkout out the docs
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
db = SQLAlchemy()
db_name = "database.db"

# there is no hope


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

class word_diffuclty(db.Model):
    __tablename__ = "difficulty"
    word_id = db.Column(db.Integer, primary_key=True)
    hard = db.Column(db.String)
    medium = db.Column(db.String)
    easy = db.Column(db.String)

class time(db.Model):
    __tablename__ = "clock"
    word2_id = db.Column(db.Integer, primary_key=True)
    ran_out=db.Column(db.String)
    on_time = db.Column(db.string)


    
    
    
    













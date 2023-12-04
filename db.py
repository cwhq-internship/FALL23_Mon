from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
db_name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)
    
    with app.app_context():
        # Define models within the app context
        class WordDifficulty(db.Model):
            __tablename__ = "difficulty"
            word_id = db.Column(db.Integer, primary_key=True)
            hard = db.Column(db.String(50))
            medium = db.Column(db.String(50))
            easy = db.Column(db.String(50))

        class Time(db.Model):
            __tablename__ = "clock"
            word2_id = db.Column(db.Integer, primary_key=True)
            ran_out = db.Column(db.String(50))
            on_time = db.Column(db.String(50))

        # Create the tables
        db.create_all()
    
    return app

#I HAVE SETUP THE DATABASE I REPEAT THERE IS A DATABASE... i just need to figure out how to update the database with every typing test logged.


    
    
    
    













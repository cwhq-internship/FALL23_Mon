from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from Google import Create_service
# I'm so sorry for what is going to proceed this josh

API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service = Create_Service(API_SERVICE_NAME, API_VERSION, SCOPES)
sheets_file1 = service.spreadsheets().create().execute()

sheet_body = {
    'properties': {
        'title' : 'Difficulty',
        'locale': 'en_US',
        'timeZone': 'America/Los_Angeles',
        'autoRecalc': 'HOUR'
    }

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

#bonejaw


    
    
    
    













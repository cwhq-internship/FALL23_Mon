from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

def Create_Service(name, version, scopes):
    return None

API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service = Create_Service(API_SERVICE_NAME, API_VERSION, SCOPES)

sheet_body = {
    'properties': {
        'title': 'Difficulty',
        'locale': 'en_US',
        'timeZone': 'America/Los_Angeles',
        'autoRecalc': 'HOUR'
    }
}

db = SQLAlchemy()
db_name = "database"
class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(255))
    wpm = db.Column(db.Float)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

class TestCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def increment_count(self):
        self.count += 1
        db.session.commit()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
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

        db.create_all()

        def log_typing_test_data(data):
            new_word_difficulty = WordDifficulty(
                hard=data.get('hard'),
                medium=data.get('medium'),
                easy=data.get('easy')
            )
            db.session.add(new_word_difficulty)
            db.session.commit()

        test_data = {
            'hard': 'Difficult word',
            'medium': 'Medium word',
            'easy': 'Easy word'
        }
        log_typing_test_data(test_data)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
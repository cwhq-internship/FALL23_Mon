from flask_sqlalchemy import SQLAlchemy
from flask import Flask

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
db_name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppresses SQLAlchemy modification tracking

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

        # Create the tables
        db.create_all()

        # Function to log typing test data into the database
        def log_typing_test_data(data):
            new_word_difficulty = WordDifficulty(
                hard=data.get('hard'),
                medium=data.get('medium'),
                easy=data.get('easy')
            )
            db.session.add(new_word_difficulty)
            db.session.commit()

        # Example usage of log_typing_test_data function
        test_data = {
            'hard': 'Difficult word',
            'medium': 'Medium word',
            'easy': 'Easy word'
        }
        log_typing_test_data(test_data)

    return app

# Run the application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

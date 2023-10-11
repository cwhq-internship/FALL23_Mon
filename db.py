from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# For more information about database configuration checkout out the docs
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
db = SQLAlchemy()
db_name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

from os import environ, getenv, scandir
from flask import render_template
from db import create_app, db
from blueprints.errors import errors_bp
from blueprints.api import api_bp
from seed import create_data

### IMPORTANT ###
# Avoid Adding routes directly to this file. New routes should be added to a new or existing
# blueprint when possible. Blueprints can be found in the blueprints folder.
app = create_app()

# Update the secret key if deploying to production
app.secret_key = 'Bruce Wayne is Batman'

# Register Blueprints here
app.register_blueprint(errors_bp)
app.register_blueprint(api_bp, url_prefix="/api")


@app.route('/')
def index():
    return render_template('home.html')


# Custom CLI Commands
# Do not update these commands without direction from your instructor
# https://flask.palletsprojects.com/en/2.1.x/cli/#custom-commands

@app.cli.command("db:drop")
def drop_database():
    "Drops the database tables"
    print("Dropping Database")
    db.drop_all()


@app.cli.command("db:create")
def create_database():
    "Creates the database tables"
    print("Creating Tables if not exist Database")
    import_models()
    for table in db.metadata.tables:
        print(table)

@app.cli.command("db:seed")
def seed_database():
    "Seeds the database with data"
    create_data()

@app.cli.command("db:reset")
def reset_database():
    import_models()
    "Re-creates tables and seeds database"
    print("Dropping all Tables")
    # db.drop_all()
    print("Creating tables")
    db.create_all()
    for table in db.metadata.tables:
        print(f'- {table}')
    print("Seeding database")
    create_data()


def import_models():
    "Used to importing models for creating database tables"
    for entry in scandir('models'):
        if entry.is_file() and entry.name.__contains__(".py"):
            filename = entry.name.replace(".py", "")
            try:
                exec(f'from models.{filename} import {filename.capitalize()}')
            except:
                print(f"""
                    Error importing model from {entry.path}. \n
                    Check the naming of your file and model
                """)


# Do not alter this if statement below unless instructed to do so
# This should stay towards the bottom of this file
if __name__ == "__main__":
    flask_env = getenv('FLASK_ENV')
    if flask_env != 'production':
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        environ['FLASK_DEBUG'] = 'development'
        app.debug = True
        app.asset_debug = True
    app.run()

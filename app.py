import flask
import wonderwords
from os import environ, getenv, scandir
from sqlalchemy import desc
from flask import render_template, request, url_for, session, jsonify, redirect
from db import create_app, db, TestResult
from blueprints.errors import errors_bp
from blueprints.api import api_bp
from seed import create_data
from words import create_sentence, easy_words, hard_words, medium_words
from arrays import easywords, mediumwords, hardwords
import json

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

@app.route('/404')
def error():
    return render_template('404.html')

@app.route('/cwhq')
def wizard():
    return render_template('cwhq.html')

@app.route('/typing')
def typing():
    return render_template('typing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/typegame')
def typegame():
    return render_template('typegame.html')

@app.route('/testeasy')
def testeasy():
    
    word_list = easy_words()
    data = json.dumps(word_list)
    return render_template('testeasy.html',data=data)

@app.route('/testmedium', methods=['GET', 'POST'])
def testmedium():
    word_list = medium_words()
    data = json.dumps(word_list)
    if request.method == 'POST':
        test_name = request.form['test_name']
        wpm = float(request.form['wpm'])
        test_result = TestResult(test_name=test_name, wpm=wpm)
        db.session.add(test_result)
        db.session.commit
    return render_template('testmedium.html',data=data)

@app.route('/reset_wpm')
def reset_wpm():
    try:
        db.session.query(TestResult).delete()
        db.session.commit()
    except Exception as e:
        print(f"Error resetting WPM: {e}")
        db.session.rollback()

    return redirect(url_for('stats'))

@app.route('/get_top_wpm')
def get_top_wpm():
    top_result = TestResult.query.order_by(desc(TestResult.wpm)).first()
    top_wpm = top_result.wpm if top_result else None
    return jsonify({'top_wpm': top_wpm})

@app.route('/get_test_counts')
def get_test_counts():
    easy_count = TestResult.query.filter_by(test_name='Easy').count()
    medium_count = TestResult.query.filter_by(test_name='Medium').count()
    hard_count = TestResult.query.filter_by(test_name='Hard').count()

    return jsonify({
        'easy_count': easy_count,
        'medium_count': medium_count,
        'hard_count': hard_count
    })

@app.route('/get_average_wpm')
def get_average_wpm():
    average_wpm = db.session.query(db.func.avg(TestResult.wpm)).scalar()
    return jsonify({'average_wpm': average_wpm})


@app.route('/submit_test_result', methods=['POST'])
def submit_test_result():
    if request.method == 'POST':
        wpm = float(request.form.get('wpm'))
        difficulty = request.form.get('difficulty')
        test_result = TestResult(test_name=difficulty, wpm=wpm)
        db.session.add(test_result)
        db.session.commit()

        return jsonify(success=True)

    return jsonify(success=False)

@app.route('/recent_results')
def recent_results():
    recent_results = TestResult.query.order_by(TestResult.date.desc()).limit(4).all()

    results_json = [
        {'test_name': result.test_name, 'wpm': result.wpm, 'date': result.date.strftime('%Y-%m-%d')}
        for result in recent_results
    ]

    return jsonify(results_json)

@app.route('/get_recent_wpm')
def get_recent_wpm():
    recent_wpm_results = TestResult.query.order_by(TestResult.date.desc()).limit(10).all()

    recent_wpm_data = {
        f'Test {i + 1}': result.wpm
        for i, result in enumerate(recent_wpm_results)
    }

    return jsonify(recent_wpm_data)


@app.route('/testhard')
def testhard():
    word_list = hard_words()
    data = json.dumps(word_list)
    return render_template('testhard.html', data=data)

@app.route('/paragraph')
def paragraph():
    return render_template('paragraph.html')

@app.route('/stats')
def stats():
    test_results = TestResult.query.all()
    top_wpm = test_results[0].wpm if test_results else None
    return render_template('stats.html', test_results=test_results, top_wpm=top_wpm)

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

# THIS IS A NOTE RAAAAAAAAAAAAAAA
# Do not alter this if statement below unless instructed to do so RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# This should stay towards the bottom of this file
if __name__ == "__main__":
    flask_env = getenv('FLASK_ENV')
    if flask_env != 'production':
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        environ['FLASK_DEBUG'] = 'development'
        app.debug = True
        app.asset_debug = True
    app.run()
#NOTES

#Master Peter was here!!
#Josh again
#Master Peter was here!!

#Medhin was hereeeeeeeeeeeeee
#josh
#Daniel was not here
# Peter destroyed everything
#Kathleen was here
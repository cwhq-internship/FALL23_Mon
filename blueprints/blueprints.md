# Getting started making flask blueprints

## What are blueprints?
Blueprints are a way for us to break apart routes into smaller easier to work with files that we can import into our flask application. This also helps prevent merge conflicts created from people working in the same files.

## Making your first blueprint
To get started simply create a new python file in the blueprints folder. Copy the following code a quick starter template and paste that into your python file. Make sure to change everywhere you see `blueprint_name_here` to the name of your blueprint.
```
from flask import Blueprint
blueprint_name_here_bp = Blueprint('blueprint_name_here', __name__)
@blueprint_name_here_bp.route('/')
def index():
    return "Hello Flask Blueprints"
```
To register the blueprint you will need to open the app.py file import your blueprint towards the top of the app.py file and then register your blueprint where the other blueprints are registered. As an example `app.register_blueprint(blueprint_name_here)`. You may want to add a route prefix to keep your blueprint from overriding other routes. To do this simple add `url_prefix` and set the prefix you would like. For example `app.register_blueprint(blueprint_name_here, url_prefix="/myroute")`

You can find the official blueprint docs [here](https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints) for more information. 

# Add decorators for routes to this file
from flask import request, redirect, url_for, session, abort
from functools import wraps


def request_args(f):
    "Passes all the form data submitted to a route directly to a route function"
    @wraps(f)
    def decorated_function():
        if request.is_json:
            json = request.get_json()
            return f(**json)
        if request.method in ['GET']:
            return f(**request.args)
        else:
            return f(**request.form)
    return decorated_function


def jsonify(f):
    "Makes the return JSON format"
    @wraps(f)
    def decorated_function():
        pass
    return None

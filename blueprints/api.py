# Use this blueprint to add API endpoints.
# Freely Remove or Update the default routes when needed

from flask import Blueprint, render_template, current_app, request, jsonify
from utils.route_decorators import request_args

api_bp = Blueprint('api', __name__)

# Example 
@api_bp.route('/')
def example_hello():
    return jsonify({
        "msg": "hello world"
    })

# Example: 
@api_bp.route('/')
@request_args
def example_message(msg):
    return jsonify({
        "msg": msg
    })

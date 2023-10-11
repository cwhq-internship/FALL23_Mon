# Use this blueprint to build error pages if required.
# A link to the most common http status codes can be found below
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# Flask Official Docs for Error Handlers
# https://flask.palletsprojects.com/en/2.1.x/errorhandling/#error-handlers

from flask import Blueprint, render_template, current_app, request

errors_bp = Blueprint('error', __name__)


@errors_bp.app_errorhandler(404)
def not_found(e):
    url = request.base_url
    current_app.logger.info(f"{url} is not a valid route")
    return render_template('404.html'), 404

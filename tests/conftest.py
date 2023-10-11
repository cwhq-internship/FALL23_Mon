# Do not update this file unless instructed to by your instructor.
# This file is for setting up tests for pytest and allows tests
# to access the flask application

import pytest

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

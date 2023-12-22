import os

import pytest

from app.extensions import db, login_manager, cors
from app import create_app

@pytest.fixture(scope='session', autouse=True)
def setup_app():

    # Set the app to testing mode connect to localhost
    os.environ['FLASK_ENV'] = 'development'
    # os.setenv('FLASK_ENV', 'development')

    app = create_app()  # replace 'testing' with your actual testing config
    # db.init_app(app)

    with app.app_context():
        yield app

@pytest.fixture()
def client(setup_app):
    return setup_app.test_client()


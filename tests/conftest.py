import os

import pytest

from app.extensions import db, login_manager, cors
from app import create_app

# The "autouse=True" means that this fixture will be automatically used by all the tests.
@pytest.fixture(scope='session', autouse=True)
def setup_app():

    # Set the app to testing mode connect to localhost
    ## if FLASK_ENV is set to 'development' in the environment, in containers it will be set to localhost instead of db
    #os.environ['FLASK_ENV'] = 'development'
    # os.setenv('FLASK_ENV', 'development')

    app = create_app()  # replace 'testing' with your actual testing config
    # db.init_app(app)

    with app.app_context():
        yield app

@pytest.fixture()
def client(setup_app):
    return setup_app.test_client()


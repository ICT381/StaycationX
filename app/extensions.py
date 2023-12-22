from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_cors import CORS, cross_origin

login_manager = LoginManager()
db = MongoEngine()
cors = CORS(resources={r"/api/*": {"origins": "*"}})
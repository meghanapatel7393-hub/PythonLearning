from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager #JWT does NOT need Flask-Login, and Flask-Login requires extra setup.
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
# login_manager = LoginManager()
jwt = JWTManager()
# login_manager.login_view = "login"
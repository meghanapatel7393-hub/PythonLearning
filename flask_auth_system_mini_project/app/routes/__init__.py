from flask import Blueprint

routes = Blueprint("routes", __name__)

from app.routes import auth
from app.routes import upload
# from app.routes import dashboard

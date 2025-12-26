from flask import Flask
from config import Config
from .extensions import db, bcrypt, jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # ✅ Only ONE blueprint
    from app.routes import routes
    app.register_blueprint(routes)

    return app


# from flask import Flask
# from config import Config
# from .extensions import db, bcrypt, jwt


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     # login_manager.init_app(app)
#     jwt.init_app(app)

#     from app.routes import routes
#     app.register_blueprint(routes)


#     return app

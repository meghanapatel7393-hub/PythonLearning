from flask import Blueprint, request,  render_template
from app.models import User
from app.extensions import db
from app.routes import routes
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

# routes = Blueprint("routes", __name__)

# @routes.route("/", methods=["GET"])
# def home():
#     return "Flask Auth System Running Successfully 🚀"


# ---------------- HOME (LOGIN PAGE)
@routes.route("/", methods=["GET"])
def home():
    return render_template("login.html")


# ---------------- REGISTER PAGE
@routes.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

# ---------------- LOGIN (JWT)
# @routes.route("/api/login", methods=["POST"])
# def api_login():
#     data = request.get_json()

#     user = User.query.filter_by(email=data["email"]).first()

#     if user and user.check_password(data["password"]):
#         token = create_access_token(identity=user.id)

#         return jsonify({
#             "success": True,
#             "token": token,
#             "user": {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email
#             }
#         })

#     return jsonify({"success": False, "message": "Invalid credentials"}), 401


# ---------------- LOGIN API
@routes.route("/api/login", methods=["POST"])
def login():
    data = request.form

    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"]):
        # token = create_access_token(identity=user.id)
        token = create_access_token(identity=str(user.id))

        return render_template(
            "uploadpage.html",
            user=user,
            token=token
        )

    return render_template("login.html", error="Invalid credentials")

# ---------------- REGISTER API
@routes.route("/api/register", methods=["POST"])
def register():
    data = request.form

    user = User(
        name=data["name"],
        email=data["email"]
    )
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return render_template("login.html", success="Registered successfully!")

# ---------------- DASHBOARD (JWT Protected)
@routes.route("/dashboard")
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return render_template("dashboard.html", user=user)

@routes.route("/uploadpage")
@jwt_required()
def uploadpage():
    return render_template("uploadpage.html")

# ---------------- REGISTER
# @routes.route("/api/register", methods=["POST"])
# def api_register():
#     data = request.get_json()

#     user = User(
#         name=data["name"],
#         email=data["email"]
#     )
#     user.set_password(data["password"])

#     db.session.add(user)
#     db.session.commit()

#     return jsonify({"message": "User registered successfully"})


# ---------------- PROTECTED ROUTE
# @routes.route("/api/dashboard", methods=["GET"])
# @jwt_required()
# def dashboard():
#     user_id = get_jwt_identity()
#     user = User.query.get(user_id)

#     return jsonify({
#         "message": "Welcome to dashboard",
#         "user": {
#             "id": user.id,
#             "name": user.name,
#             "email": user.email
#         }
#     })

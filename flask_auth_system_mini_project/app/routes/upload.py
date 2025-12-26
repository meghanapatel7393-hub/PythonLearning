import os
from flask import request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from app.routes import routes
from app.models import User
from app.extensions import db

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@routes.route("/upload-image", methods=["POST"])
@jwt_required(optional=True)
def upload_image():
    if "image" not in request.files:
        return {"error": "No image uploaded"}, 400

    file = request.files["image"]

    if not allowed_file(file.filename):
        return {"error": "Invalid file type"}, 400

    filename = secure_filename(file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    user_id =int(get_jwt_identity())# get_jwt_identity()
    user = User.query.get(user_id)
    user.image = filename
    db.session.commit()

    return {
        "message": "Image uploaded successfully",
        "file": filename
    }
    # return {"message": "Image uploaded successfully"}


# import os
# from flask import request, jsonify, current_app
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from werkzeug.utils import secure_filename
# from app.routes import routes
# # from app.routes import routes
# # from app.extensions import db
# # from app.models import User


# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# def allowed_file(filename):
#     return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# @routes.route("/upload-image", methods=["POST"])
# @jwt_required()
# def upload_image():
#     if "image" not in request.files:
#         return {"error": "No image uploaded"}, 400

#     file = request.files["image"]

#     if not allowed_file(file.filename):
#         return {"error": "Invalid file type"}, 400

#     filename = secure_filename(file.filename)

#     upload_folder = current_app.config["UPLOAD_FOLDER"]
#     os.makedirs(upload_folder, exist_ok=True)

#     file_path = os.path.join(upload_folder, filename)
#     file.save(file_path)

#     user_id = get_jwt_identity()
#     user = User.query.get(user_id)
#     user.image = filename

#     db.session.commit()

#     return {
#         "message": "Image uploaded successfully",
#         "file": filename
#     }

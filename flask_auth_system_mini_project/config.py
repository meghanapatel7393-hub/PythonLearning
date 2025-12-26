import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load .env file
load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# password = quote_plus(os.getenv("DB_PASS"))
if not db_pass:
    raise ValueError("DB_PASS not found. Check your .env file.")

encoded_password = quote_plus(db_pass)

class Config:
    SECRET_KEY = "supersecret"
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{db_user}:{encoded_password}@{db_host}/{db_name}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "jwt-secret"
    UPLOAD_FOLDER = "app/static/uploads"
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Bhavesh%401234@localhost:3306/flask_auth"
    # SQLALCHEMY_DATABASE_URI = (
    #     f"mysql+pymysql://{os.getenv('DB_USER')}:{password}"
    #     f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    # )
   

#for SQLite
# SQLALCHEMY_DATABASE_URI = "sqlite:///database.db" SQLite
#this database setup is MySQL
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/flask_auth"

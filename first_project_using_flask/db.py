import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# //working to connect db
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Bhavesh@1234",
#     database="python_db"
# )

# cursor = db.cursor()

# cursor.execute("SELECT DATABASE()")
# print("Connected to:", cursor.fetchone())

# Step 10: Create Database in MySQL
# first need In MySQL Workbench or cmd:
# CREATE DATABASE python_db;
# USE python_db;

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100)
# );

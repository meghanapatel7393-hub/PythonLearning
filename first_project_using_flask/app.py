from flask import Flask, render_template, request, jsonify
from db import get_db_connection

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello Flask Backend"

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    if request.method == "POST":
        name = request.form.get("username")
    return render_template("formpage.html", name=name)

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello")
def hello():
    return "Hello User"


# users = {}  # temporary storage

@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db_connection()
        cursor = db.cursor()

        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, username+"@gmail.com", password))
        db.commit()
        # users[username] = password
        message = "Registered successfully!"
    return render_template("register.html", message=message)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    user_data = None 

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM users WHERE name = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            message = "Login successful"
            user_data = user
        else:
            message = "Invalid credentials"
    
    return render_template(
        "login.html",
        message=message,
        user=user_data
    )

        # if user:
        #     message= jsonify({"message": "Login successful", "user": user})
        # else:
        #     message = jsonify({"message": "Invalid credentials"}), 401

        # if users.get(username) == password:
        # if user:
        #     message = "Login successful!"
        # else:
        #     message = "Invalid credentials"
    # return render_template("login.html", message=message)


# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     return f"Welcome {data['username']}"

@app.route("/api/user")
def user():
    return jsonify({
        "name": "Bhavesh",
        "role": "Backend Dev"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(debug=True)

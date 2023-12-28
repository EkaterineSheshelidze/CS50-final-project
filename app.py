import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///giveradar.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/welcome")
def welcome():
    """Welcome page"""

    session.clear()
    if session.get("user_id") is None:
        return render_template("welcome.html", welcome=True)
    else:
        return redirect("/")


@app.route("/")
@login_required
def index():
    """Display user info and progress on home page"""

    user = db.execute(
        "SELECT * FROM users WHERE id = ?", session["user_id"]
    )
    
    progress = db.execute(
        "SELECT * FROM progress WHERE person_id = ? ORDER BY date DESC", session["user_id"]
    )
    return render_template("index.html", user=user[0], progress=progress)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add new progress"""

    if request.method == "POST":
        # Get user input
        orgName = request.form.get("org_name")
        progressType = request.form.get("type")
        progressDate = request.form.get("date")
        hours = request.form.get("hours")

        # Ensure everything was submitted corrrectly
        if not orgName or not progressType or not progressDate or not hours:
            return apology("add.html", "Fill out all fields")
        elif not hours.isnumeric() or float(hours) <= 0:
            return apology("add.html", "Provide positive number of hours")

        hours = float(hours)
        points = hours * 20

        # Insert to progress
        db.execute(
                "INSERT INTO progress (person_id, orgName, type, date, hours, points) VALUES(?, ?, ?, ?, ?, ?)",
                session["user_id"],
                orgName,
                progressType,
                progressDate,
                hours,
                points,
        )

        userHours = db.execute("SELECT hours FROM users WHERE id = ?", session["user_id"])
        userPoints = db.execute("SELECT points FROM users WHERE id = ?", session["user_id"])
        newHours = float(userHours[0]["hours"]) + hours
        newPoints = float(userPoints[0]["points"]) + points

        # Update user hours and points
        db.execute(
            "UPDATE users SET hours = ?, points = ? WHERE id = ?", 
            newHours,
            newPoints,
            session["user_id"],
        )

        return redirect("/")
    else:
        return render_template("add.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("login.html", "Fill out username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("login.html", "Fill out password")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("login.html", "Wrong username or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Get username and password
        username = request.form.get("username")
        password = request.form.get("password")

        # Check username and password
        if not username:
            return apology("register.html", "Fill out username")
        elif db.execute("SELECT username FROM users WHERE username = ?", username):
            return apology("register.html", "Username already exists")
        elif not password:
            return apology("register.html", "Fill out password")
        elif password != request.form.get("confirmation"):
            return apology("register.html", "Confirm password")

        # Register user
        db.execute(
            "INSERT INTO users (username, password) VALUES(?, ?)",
            username,
            generate_password_hash(password),
        )

        return redirect("/")

    else:
        return render_template("register.html")
    

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Open profile page"""
    return render_template("profile.html")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change password"""

    if request.method == "POST":
        # Get user input
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Get current password
        current_password = db.execute(
            "SELECT password FROM users WHERE id = ?", session["user_id"]
        )

        # Check user input
        if not old_password or not new_password or not confirmation:
            return apology("password.html", "Fill out all fields")
        elif not check_password_hash(current_password[0]["password"], old_password):
            return apology("password.html", "Wrong old password")
        elif new_password != confirmation:
            return apology("password.html", "Confirm new password")

        # Update password
        db.execute(
            "UPDATE users SET password = ? WHERE id = ?",
            generate_password_hash(new_password),
            session["user_id"],
        )

        return redirect("/")

    else:
        return render_template("password.html")
    
    
@app.route("/upload", methods=["POST"])
@login_required
def upload_profile_pic():
    """Change profile picture"""

    # Get the uploaded file
    profile_pic = request.files["profile_pic"]

    # Ensure profile_pic was submitted
    if not profile_pic:
        return apology("profile.html", "Upload profile picture")

    # Extract filename and save to database
    filename = profile_pic.filename
    db.execute("UPDATE users SET pic = ? WHERE id = ?", filename, session["user_id"])

    # Save the file to uploads
    profile_pic.save("static/uploads/" + filename)

    return redirect("/")


@app.route("/discover")
@login_required
def discover():
    """Display news on discover page"""

    # Get news form discover
    news = db.execute(
        "SELECT * FROM discover"
    )

    return render_template("discover.html", news=news)


@app.route("/map")
@login_required
def map():
    """Open map page"""
    return render_template("map.html")

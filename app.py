from flask import Flask, render_template, request, redirect, url_for
from cs50 import SQL

app = Flask(__name__)

# Establish a connection to the SQLite database
db = SQL("sqlite:///registrants.db")

# Predefined list of sports
SPORTS = ["Basketball", "Soccer", "Baseball", "Tennis", "Cricket", "Rugby", "Golf", "Swimming", "Cycling", "Badminton"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    # Validation
    if not name or sport not in SPORTS:
        return render_template("failure.html")

    # Insert into the database
    db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)

    # Return the register confirmation page
    return render_template("register.html", name=name, sport=sport)

@app.route("/registrants")
def registrants():
    rows = db.execute("SELECT name, sport FROM registrants")
    return render_template("registrants.html", registrants=rows)

if __name__ == '__main__':
    app.run(debug=True)

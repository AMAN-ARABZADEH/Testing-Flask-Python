from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}
SPORTS = ["Basketball", "Soccer", "Baseball", "Tennis", "Cricket", "Rugby", "Golf", "Swimming", "Cycling", "Badminton"]


@app.route("/")

def index():
    return render_template("index.html", sports=SPORTS)

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    sport = request.form.get("sport")
    if sport not in SPORTS:
        return render_template("failure.html")
    REGISTRANTS[name] = sport
    return render_template("register.html", name = name, sport = sport)

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", REGISTRANTS=REGISTRANTS)


if __name__ == '__main__':
    app.run(debug=True)
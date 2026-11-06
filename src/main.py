from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/")
def root():
    with open("./pages/root.html", "r") as f:
        return f.read()


@app.route("/login")
def login():
    with open("./pages/login.html", "r") as f:
        return f.read()


@app.route("/api/submit", methods=["GET", "POST"])
def api_submit():
    if request.method == "POST":
        DATA = {"username": request.form["username"]}
        print(f"\n===\nSubmitted username: {DATA['username']}\n===\n")
        return f"Username logged in: {DATA['username']}"
    else:
        return redirect("/login")

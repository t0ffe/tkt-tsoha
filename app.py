from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/add_item")
def add_item():
    return render_template("add_item.html")

def addBadge():
    return

def removeBadge():
    return

def updateBadge():
    return


if __name__ == "__main__":
    app.run(host="127.0.0.1")
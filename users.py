from os import getenv
from db import db
from flask import session, redirect, request
from app import app

app.secret_key = getenv("SECRET_KEY")

def login(name, password):
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check credentials
    session["username"] = username
    return redirect("/")

def logout():
    del session["username"]
    return redirect("/")

def register(name, password, role):
    #TODO implement registering (with hashing)
    return login(name, password)

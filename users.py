from os import getenv
from db import db
from flask import session, redirect, request
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


app.secret_key = getenv("SECRET_KEY")

def login(name, password):
    sql = "SELECT id, password FROM users WHERE name=:name"
    result = db.session.execute(text(sql), {"name":name})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = name
            return True
        else:
            return False

def logout():
    del session["username"]
    return redirect("/")

def register(name, password1, password2, role):

    if password1 != password2:
        return False

    hash_value = generate_password_hash(password1)

    sql = "INSERT INTO users (name, password, role) VALUES (:name, :password, :role)"
    db.session.execute(text(sql), {"name":name, "password":hash_value, "role":role})
    db.session.commit()

    return login(name, password1)

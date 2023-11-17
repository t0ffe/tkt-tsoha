from app import app
from flask import redirect, render_template, request, jsonify
import badges
import collections
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error/<string:e>")
def error(e):
    return render_template("error.html", error=e)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/add_badge', methods=['GET', 'POST'])
def addBadge():
    if request.method == 'GET':
        return render_template('add_badge.html')
    
    if request.method == 'POST':
        
        collection_id = request.form["collection_id"]
        amount = request.form["amount"]
        price = request.form["price"]
        name = request.form["name"]
        designer = request.form["designer"]
        supplier = request.form["supplier"]
        
        result = badges.add_badge(collection_id, amount, price, name, designer, supplier)

        return result
        
def removeBadge():
    return

def updateBadge():
    return
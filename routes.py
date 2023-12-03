from app import app
from flask import redirect, render_template, request, jsonify
import badges
import users
import orgs

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error/<string:e>")
def error(e):
    return render_template("error.html", error=e)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return redirect("/error/<Väärä tunnus tai salasana>")
        return redirect("/login")
    
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        #TODO implement registering
        users.register(request.form["username"], request.form["password1"], request.form["role"])
        return redirect("/login")



@app.route('/add_badge', methods=['GET', 'POST'])
def addBadge():
    if request.method == 'GET':
        return render_template('add_badge.html')
    
    if request.method == 'POST':
        student_organization = request.form["student_organization"]
        amount = request.form["amount"]
        price = request.form["price"]
        name = request.form["name"]
        designer = request.form["designer"]
        supplier = request.form["supplier"]
        
        badges.add_badge(student_organization, amount, price, name, designer, supplier)

        return redirect("add_badge")

@app.route('/add_student_org', methods=['GET', 'POST'])
def addStudentOrg():
    if request.method == 'GET':
        return render_template('add_student_org.html')
    
    if request.method == 'POST':
        student_organization = request.form["student_organization"]
        orgs.add_org(student_organization)

        return redirect("login")

        
def removeBadge():
    return

def updateBadge():
    return
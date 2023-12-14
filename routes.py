from app import app
from flask import redirect, render_template, request, jsonify, url_for
import badges
import users
import orgs

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        minimal_badges_ = badges.getAllBadges()
        return render_template("index.html", minimal_badges=minimal_badges_,count=len(minimal_badges_))
    
    if request.method == "POST":
        badge_id = request.form["badge_id"]
        print("BADGE ID", badge_id)
        return redirect(url_for('.editBadge', badge_id=badge_id))

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
        orgs_ = orgs.getAllOrgs()
        suppliers_ = badges.getAllSuppliers()
        designers_ = badges.getAllDesigners()
        return render_template('add_badge.html', student_organizations=orgs_, designers=designers_, suppliers=suppliers_)
    
    if request.method == 'POST':
        student_organization = request.form["student_organization"]
        amount = request.form["amount"]
        price = request.form["price"]
        name = request.form["name"]
        designer = request.form["designer"]
        supplier = request.form["supplier"]
        
        badges.add_badge(student_organization, amount, price, name, designer, supplier)

        return redirect("add_badge")
    
@app.route('/edit_badge', methods=['GET', 'POST'])
def editBadge():
    if request.method == 'GET':
        print("FIRST LINE")
        badge_id = request.args["badge_id"]
        print(badge_id)
        badge = badges.getOneBadge(badge_id)
        print(badge)
        return render_template('edit_badge.html', id=badge[0], name=badge[1], amount=badge[2], price=badge[3])
    
    if request.method == 'POST':
        amount = request.form["amount"]
        price = request.form["price"]
        name = request.form["name"]
        id = request.form["badge_id"]
        
        badges.updateBadge(id, name, amount, price)

        return redirect("/")

@app.route('/add_student_org', methods=['GET', 'POST'])
def addStudentOrg():
    if request.method == 'GET':
        return render_template('add_student_org.html')
    
    if request.method == 'POST':
        student_organization = request.form["student_organization"]
        orgs.addOrg(student_organization)

        return redirect("login")

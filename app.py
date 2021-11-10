import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# welcome page function
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


# register page function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Email already exists")
            return redirect(url_for("register"))

        new_user = {
            "name": request.form.get("name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "image": request.form.get("image")
        }
        mongo.db.users.insert_one(new_user)
        
        # put new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", email=session['user']))
    return render_template("register.html")


# login page function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("email").lower()
                    flash("Login Successful".format(request.form.get("email")))
                    return redirect(url_for("profile", email=session['user']))
            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")  


# Profile Page function
@app.route("/profile/<email>", methods=["GET", "POST"])
def profile(email):
    # grab the session user's email from db
    email = mongo.db.users.find_one(
        {"email": session["user"]})["email"]
    if session["user"]:    
        return render_template("profile.html", email=email)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# display recipe function
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
      # recipe id don't exist, show 404 error
    if not recipe:
        return render_template("error_handlers/404.html")
    return render_template("show_recipe.html", recipe=recipe)


# Adding recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))
    return render_template("add_recipe.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
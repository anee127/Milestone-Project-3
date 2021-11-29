import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # file sizes under 2mb

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# welcome page function


@app.route("/")
@app.route("/homepage")
def homepage():
    index = list(mongo.db.recipes.find())
    return render_template("index.html", index=index)


# register page function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "image": request.form.get("image")
        }
        mongo.db.users.insert_one(new_user)

        # put new user into 'session' cookie
        # use object Id for session user
        session["user"] = request.form.get("username")
        flash("Registration Successful")
        return redirect(url_for("profile", username=session['user']))
    return render_template("register.html")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Profile secion
# login page function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Login Successful".format(request.form.get("username")))
                return redirect(url_for("profile", username=session['user']))
            else:
                # invalid password match  -----
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Profile Page function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        user_recipes = list(
            mongo.db.recipes.find({"created_by": session["user"]})
        )
        return render_template("profile.html", username=user, user_recipes=user_recipes)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Recipes secion

# display recipe function


@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})

    return render_template(
        'show_recipe.html',
        recipe=recipe,
    )

# all recipes function
@app.route("/all_recipes", methods=["GET"])
def all_recipes():
    # grab the session user's username from db
       
    recipes = list(
        mongo.db.recipes.find()
    )
    return render_template("all_recipes.html", recipes=recipes)


# search recipe function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("all_recipes.html", recipes=recipes)  

# Adding recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if not session.get("user"):
        return render_template("error_handlers/404.html")

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_serves": request.form.get("recipe_serves"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session['user']))
    return render_template("add_recipe.html")


# Editing Recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    if not session.get("user"):
        return render_template("error_handlers/404.html")

    if request.method == "POST":
        recipe_info = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_serves": request.form.get("recipe_serves"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe_info)
        flash("Recipe Successfully Changed")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("edit_recipe.html", recipe=recipe)

# Deleting Recipe function


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Delete recipe from db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe succesfully Deleted")
    return redirect(url_for("get_recipes", username=session['user']))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

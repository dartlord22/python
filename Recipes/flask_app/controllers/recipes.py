from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/recipes")
def user_recipes():
    user = User.get_by_id({"id":session["user_id"]})
    session['user_id'] = user.id
    if 'user_id' not in session:
        return redirect("/user/login")
    if not user:
        return redirect("/user/logout")
    return render_template("recipes.html", user=user, recipes=Recipe.get_all())  

@app.route("/recipes/new")
def create_recipe():
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template("add_new_recipe.html")

@app.route("/recipes/new/process", methods=["POST"])
def process_recipe():
    if "user_id" not in session:
        return redirect("/user/login")
    data = {
        "user_id": session["user_id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
    }
    Recipe.save(data)
    return redirect("/recipes")
    
@app.route("/recipes/<int:id>")
def show_recipe(id):
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template("show_recipe.html", recipe=Recipe.get_by_id({"id": id}))

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template("edit_recipe.html", recipe=Recipe.get_by_id({"id": id}))

@app.route("/recipes/edit/process/<int:id>", methods=["POST"])
def process_edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made": request.form['date_made'],
        "under_30": request.form['under_30'],
    }
    Recipe.update(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    Recipe.delete({'id':id})
    return redirect('/recipes')




from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.recipe import Recipe

#===========================================================
#ROUTE TO RENDER RECIPE PAGE TEMP

@app.route("/create_recipe")
def create_recipe():
    if "user_id" not in session:
        flash("please login/ register before entering the site!")
        return redirect("/")
    return render_template("create_recipe.html")
#===========================================================


#===========================================================

# ROUTE TO PROCESS THE CREATION

@app.route("/creating_recipe", methods =['POST'])
def creating_recipe():
    if 'under_thirty' not in request.form:
        data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'user_id' : session['user_id']
        }
        if Recipe.validate_Recipe(request.form):
            Recipe.save_Recipe(data)
            return redirect("/user")
    else:
        #Validate the FORM
        data = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instructions' : request.form['instructions'],
            'date_made' : request.form['date_made'],
            'under_thirty' : request.form['under_thirty'],
            'user_id' : session['user_id']
        }
        
        if Recipe.validate_Recipe(request.form):
            Recipe.save_Recipe(data)
            return redirect("/user")
    return redirect("/create_recipe")

#===========================================================

@app.route('/user/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/user')

#========================================================

#ROUTE to update the owner info

@app.route("/update/<int:id>")
def update_owner(id):
    if "user_id" not in session:
        flash("please login/ register before entering the site!")
        return redirect("/")
    data = {
        "id" : id
    }
    recipe = Recipe.one_Recipe(data)
    return render_template("edit_recipe.html", recipe = recipe)

#========================================================

#ROUTE to process the update 

@app.route("/updating/<int:id>", methods=['POST'])

def updating_Recipe(id):
    data = {
        'id': id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'under_thirty' : request.form['under_thirty'],
        'user_id' : session['user_id']
    }
    Recipe.update_Recipe(data)
    return redirect("/user")
#=======================================================
#View one recipe

@app.route("/recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    if "user_id" not in session:
        flash("please login/ register before entering the site!")
        return redirect("/")
    data = {
        "id" : recipe_id
    }
    recipe = Recipe.one_Recipe(data)
    return render_template("show_recipe.html", recipe = recipe)

#========================================================

from queue import Empty
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self,data):
        self.id = data['id']

        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']


        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user_id = data['user_id']
#============================================================
#validating recipe added
    @staticmethod
    def validate_Recipe(recipe):
        is_valid = True
        if 'under_thirty' not in recipe:
            flash("Select Yes or Now")
            is_valid = False
        if len(recipe['name']) < 3:
            flash("Recipe's name must be at least three characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Recipe's description must be at least three characters.")
            is_valid = False
        if recipe["date_made"] == "":
            flash("Please enter date")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Recipe's instructions must be at least three characters.")
            is_valid = False
        return is_valid

#============================================================
#SAVE CREATED RECIPE

    @classmethod
    def save_Recipe(cls, data):
        query= "INSERT INTO recipes(name, description, instructions, user_id, date_made, under_thirty, created_at, updated_at) VALUES(%(name)s,%(description)s,%(instructions)s,%(user_id)s,%(date_made)s,%(under_thirty)s,NOW(),NOW());"
        recipe_id = connectToMySQL("recipes_schema").query_db(query, data)
        return recipe_id

#=============================================================
#GET ALL RECIPES

    @classmethod
    def all_Recipes(self,data):
        query = "SELECT * From recipes"
        all_Recipes = connectToMySQL("recipes_schema").query_db(query, data)
        return all_Recipes
#============================================================

#============================================================

# show one Recipe

    @classmethod
    def one_Recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL("recipes_schema").query_db(query,data)
        return cls(results[0])

#============================================================

#============================================================
# Delete Recipe

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        clear = connectToMySQL('recipes_schema').query_db(query, data)
        return

#============================================================

# update the recipe info

    @classmethod
    def update_Recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_thirty = %(under_thirty)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL("recipes_schema").query_db(query, data)

#============================================================

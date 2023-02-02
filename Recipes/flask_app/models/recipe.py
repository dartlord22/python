from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

db = "recipes"
class Recipe:
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.name = db_data["name"]
        self.description = db_data["description"]
        self.instructions = db_data["instructions"]
        self.date_made = db_data["date_made"]
        self.under_30 = db_data["under_30"]
        self.user_id = db_data["user_id"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.creator = None #placeholder for later assignment of an object representing the creator of the recipe 
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id"
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for row in results:
            this_recipe = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": "",
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            this_recipe.creator = user.User(user_data)
            recipes.append(this_recipe)
        return recipes
        
        
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL("recipes").query_db(query, data)
        result = result[0]
        this_recipe = cls(result)
        user_data = {
                "id": result['users.id'],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "email": result["email"],
                "password": "",
                "created_at": result["users.created_at"],
                "updated_at": result["users.updated_at"]
        }
        this_recipe.creator = user.User(user_data) #when specifying classes from other files, you need to use dot notation to call out that file as seen here
        return this_recipe
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s, %(user_id)s;"
        return connectToMySQL("recipes").query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s , date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL("recipes").query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("recipes").query_db(query, data)
    
    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        if len(form_data['name']) < 4:
            flash("NAME MUST BE AT LEAST 4 CHARACTERS")
            is_valid = False
        if len(form_data['description']) < 4:
            flash("DESCRIPTION MUST BE AT LEAST 4 CHARACTERS")
            is_valid = False
        if len(form_data['instructions']) < 4:
            flash("INSTRUCTIONS MUST BE AT LEAST 4 CHARACTERS")
            is_valid = False
        if form_data['date_made'] == '':
            flash("DATE MADE IS A REQUIRED FIELD")
            is_valid = False
        if 'under_30' not in form_data:
            flash("UNDER 30? IS A REQUIRED FIELD")
            is_valid = False
        return is_valid
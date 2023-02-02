from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
#from flask_app import bcrypt
import re

db = "recipes"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.first_name = db_data["first_name"]
        self.last_name = db_data["last_name"]
        self.email = db_data["email"]
        self.password = db_data["password"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        
    @classmethod
    def save(cls, form_data):
        hashed_data = {
            "first_name": form_data["first_name"],
            "last_name": form_data["last_name"],   
            "email": form_data["email"],
            "password": form_data["password"], #taking out bcrypt until I can get it to work 
        }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(db).query_db(query, hashed_data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, data)
        if not result:
            return False
        return cls(result[0]) #when getting a single result, we are ordering our data based on the value we are inputting (for instance, id)
                              #this result[0] will grab the top result which is the one we want
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        if not result:
            return False
        return cls(result[0]) #when getting a single result, we are ordering our data based on the value we are inputting (for instance, id)
                              #this result[0] will grab the top result which is the one we want 
    

    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        if len(form_data["email"]) < 1:
            flash("EMAIL IS A REQUIRED FIELD.", "register") #register reefers to a category in our form
            is_valid = False
        elif not EMAIL_REGEX.match(form_data["email"]):
            flash("INVALID EMAIL.", "register")
            is_valid = False
        elif User.get_by_email(form_data):
            flash("EMAIL ALREADY IN USE.", "register")
            is_valid = False
        if len(form_data["password"]) < 4:
            flash("PASSWORD MUST BE AT LEAST 4 CHARACTERS.", "register")
            is_valid = False
        if form_data["password"] != form_data["confirm_password"]:
            flash("PASSWORDS DO NOT MATCH.", "register")
            is_valid = False
        if len(form_data["first_name"]) < 4:
            flash("FIRST NAME MUST BE AT LEAST 4 CHARACTERS.", "register")
            is_valid = False
        if len(form_data["last_name"]) < 4:
            flash("LAST NAME MUST BE AT LEAST 4 CHARACTERS.", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form_data):
        if not EMAIL_REGEX.match(form_data["email"]):
            flash("INVALID EMAIL OR PASSWORD.", "login")
            return False

        user = User.get_by_email(form_data)
        if not user:
            flash("INVALID EMAIL OR PASWORD.", "login")
            return False       
        return user
    
    
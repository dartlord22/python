from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.tree import Tree
from flask_app import bcrypt
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DB = 'arbortrary'
class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.trees = []
        
        
    @classmethod
    def save(cls, data):
        hashed_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': bcrypt.generate_password_hash(data['password'])
        }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DB).query_db(query, hashed_data)

    @classmethod
    def get_user_info(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        if not result:
            return False
        return cls(result[0])
    
    @classmethod
    def get_one_with_trees(cls, data):
        query = "SELECT * FROM users LEFT JOIN trees on users.id = trees.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        user = cls(results[0])
        for row in results:
            data = {
                'id': row['trees.id'],
                'species': row['species'],
                'location': row['location'],
                'reason': row['reason'],
                'date_planted': row['date_planted'],
                'user_id': row['user_id'],
                'created_at': row['trees.created_at'],
                'updated_at': row['trees.updated_at']
            }
            user.trees.append(Tree(data))
        print(user.trees)
        return user

    @staticmethod
    def validate_registration(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;" 
        result = connectToMySQL(DB).query_db(query, user)
        if len(user['first_name']) < 2:
            flash('FIRST NAME MUST BE AT LEAST 2 CHARACTERS', 'registration') 
        if user['first_name'] == '':
            flash('FIRST NAME IS A REQUIRED FIELD', 'registration')
        if len(user['last_name']) < 2:
            flash('LAST NAME MUST BE AT LEAST 2 CHARACTERS', 'registration')
            is_valid = False
        if user['last_name'] == '':
            flash('LAST NAME IS A REQUIRED FIELD', 'registration')
            is_valid = False
        if len(result) >= 1:
            flash('EMAIL ALREADY IN USE', 'registration')
            is_valid = False
        if user['email'] == '':
            flash('EMAIL IS A REQUIRED FIELD', 'registration')
            is_valid = False
        if len(user['password']) < 8:
            flash('PASSWORD MUST BE AT LEAST 8 CHARACTERS', 'registration')
            is_valid = False
        if user['password'] == '':
            flash('PASSWORD IS A REQUIRED FIELD', 'registration')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('PASSWORDS DO NOT MATCH' ,'registration')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        if not EMAIL_REGEX.match(data["email"]):
            flash("INVALID EMAIL OR PASSWORD", "login")

        user = User.get_by_email(data)
        if not user: 
            flash("INVALID EMAIL OR PASSWORD", "login")
            return False
        return user
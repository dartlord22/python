from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DB = 'pencild_n'
class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.coordinator = []
        
    @classmethod
    def save(cls, data):
        hashed_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': data['password'], 
        }           
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DB).query_db(query, hashed_data)
    
    @classmethod
    def save_picture(cls, data):        
        query = "INSERT INTO users (profile_picture) VALUES (%(profile_picture)s)"
        return connectToMySQL(DB).query_db(query, data)
    
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
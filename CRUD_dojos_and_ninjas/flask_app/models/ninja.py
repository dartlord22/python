from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
        
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s, NOW(), NOW());'
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def update_ninja(cls, data):
        query = 'UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, WHERE id = %(id)s;'
        return connectToMySQL(cls.DB).query_db(query,data)
        
        
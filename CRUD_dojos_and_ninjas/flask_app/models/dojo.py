from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at'],
                'dojo_id' : row_from_db['dojo_id']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
    
    @classmethod
    def create_dojo(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
        

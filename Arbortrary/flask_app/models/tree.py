from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

DB = 'arbortrary'
class Tree:
    def __init__(self, data):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.reason = data['reason']
        self.date_planted = data['date_planted']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.planter = None #leaving this open so that we can add planters with our methods below
        #the reason we don't just have the planter stored in our trees table is to reduce data redundancy and keep our data more organized 
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM trees LEFT JOIN users on trees.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        trees = [] #made an empty list to store the tree objects created in the next loop
        for row in results:
            this_tree = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': "",
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_tree.planter = user.User(user_data)
            trees.append(this_tree)
        return trees
    #In the above code, we are looping through the list of trees, adding a planter to each tree, and then returning the full list
    
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM trees LEFT JOIN users on trees.user_id = users.id WHERE trees.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        result = result[0] #only want the top result, hence the result[0]
        tree = cls(result)
        data = {
                'id' : result['users.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'email' : result['email'],
                'password' : result['password'],
                'created_at' : result['users.created_at'],
                'updated_at': result['users.updated_at']
        }
        tree.planter = user.User(data)
        return tree
    #In the code above, we are getting the first result, adding a planter to it, and then returning the result 
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO trees (species, location, reason, date_planted, user_id) VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE trees SET species = %(species)s, location = %(location)s, reason = %(reason)s , date_planted = %(date_planted)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM trees WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @staticmethod
    def validate_tree(form_data):
        is_valid = True

        if len(form_data['species']) < 5:
            flash('SPECIES MUST BE AT LEAST 5 CHARACTERS')
            is_valid = False
        if len(form_data['species']) == '':
            flash('SPECIES IS A REQUIRED FIELD')
            is_valid = False
        if len(form_data['location']) < 2:
            flash('LOCATION MUST BE AT LEAST 2 CHARACTERS')
            is_valid = False
        if len(form_data['location']) == '':
            flash('LOCATION IS A REQUIRED FIELD')
            is_valid = False
        if len(form_data['reason']) > 50:
            flash('REASON HAS EXCEEDED THE MAX NUMBER OF CHARACTERS (50)')
            is_valid = False
        if len(form_data['reason']) == '':
            flash('REASON IS A REQUIRED FIELD')
            is_valid = False
        if form_data['date_planted'] == '':
            flash("DATE PLANTED IS REQUIRED")
            is_valid = False

        return is_valid
    
        
    
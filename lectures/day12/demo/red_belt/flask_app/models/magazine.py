from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from pprint import pprint

DATABASE = 'magazines'

class Magazine:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO magazines (title,description, user_id) VALUES (%(title)s, %(description)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
        
    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM magazines JOIN users ON users.id = magazines.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        magazines = []
        for u in results:
            magazines.append( cls(u) )
        return magazines
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM magazines JOIN users ON users.id = magazines.user_id WHERE magazines.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    
        # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE magazines SET title=%(title)s,description=%(description)s,user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
  
    @staticmethod
    def validate_magazine(magazine):
        is_valid = True
        if len(magazine['description']) < 10:
            flash("description must be at least 10 characters.")
            is_valid = False
        if len(magazine['title']) < 2:
            flash("title must be at least 2 characters.")
            is_valid = False
        return is_valid
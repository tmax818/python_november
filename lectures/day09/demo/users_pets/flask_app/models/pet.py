from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
DATABASE = 'users_crud'

class Pet:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO pets (title, last_name, email) VALUES (%(title)s, %(last_name)s, %(email)s);"    
        return connectToMySQL(DATABASE).query_db(query, data)
        
    #! READ ALL    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pets;"
        results = connectToMySQL(DATABASE).query_db(query)
        pets = []
        for pet in results:
            pets.append( Pet(pet) )
        return pets
    
    #! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM pets WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return Pet(result[0])

    #! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE pets SET title=%(title)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM pets WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
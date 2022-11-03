from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
DATABASE = 'user_pets'

class Pet:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO pets (name, type, user_id) VALUES (%(name)s, %(type)s, %(user_id)s);"    
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
        query = "UPDATE pets SET name=%(name)s, type=%(type)s, user_id=%(user_id)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM pets WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
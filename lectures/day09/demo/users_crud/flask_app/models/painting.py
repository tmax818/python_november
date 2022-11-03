from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
DATABASE = 'users_crud'

class Painting:
    
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
        query = "INSERT INTO paintings (title, last_name, email) VALUES (%(title)s, %(last_name)s, %(email)s);"    
        return connectToMySQL(DATABASE).query_db(query, data)
        
    #! READ ALL    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paintings;"
        results = connectToMySQL(DATABASE).query_db(query)
        paintings = []
        for painting in results:
            paintings.append( Painting(painting) )
        return paintings
    
    #! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM paintings WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return Painting(result[0])

    #! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE paintings SET title=%(title)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    
    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
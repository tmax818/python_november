from mysqlconnection import connectToMySQL

DATABASE = 'things'

class Thing:
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO things (title) VALUES (%(title)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
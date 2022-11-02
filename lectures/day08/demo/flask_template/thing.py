from mysqlconnection import connectToMySQL
from pprint import pprint
DATABASE = 'things'

class Thing:
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
        
    #! CREATE     
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO things (title) VALUES (%(title)s);"
        result =  connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        return result
    
    def display_title(self):
        return self.title.upper()
    
    #! READ ALL
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM things"
        results =  connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        things = []
        for thing in results:
            things.append(Thing(thing))
        pprint(things)
        return things
        
        
    
    
    #! READ ONE 
    
    
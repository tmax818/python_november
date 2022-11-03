from flask_app.config.mysqlconnection import connectToMySQL
# TODO import the Pet class to be used below
from pprint import pprint
DATABASE = 'users_crud'

class User:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        # TODO Create an instance attribute to hold all pets(i.e. a list)
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"    
        return connectToMySQL(DATABASE).query_db(query, data)
        
    #! READ ALL    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( User(user) )
        return users
    
    #! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return User(result[0])
    
    #! READ ONE WITH MANY
    
    # TODO create a class method to retrive all the pets that belong to a certain user
    # TODO write a join sql query to get a user and all its pets
    # TODO the query will be a list of dictionaries. Each dictionary will contain all the attributes of the user and one of the user's pets.
    # TODO create an instance of the user class that will have the pets attribute. The attribute is a list of all that user's pets
    # TODO loop over the list of dictionaries returned from the database.
    # TODO create a dictionary to hold and format the pet's data from each dictionary.
    # TODO append `pets.`to the attributes where needed:
    # TODO once the dictionary is created for each pets, append it to the pets attribute list. Inside the append method, convert the dictionary created in the previous step to an instance of the pet class.
    # TODO finally, return the user created above. It will contain the pets attribute created in the for loop above.

    #! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    

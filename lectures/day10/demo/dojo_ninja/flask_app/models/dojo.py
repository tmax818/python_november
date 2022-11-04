from flask_app.config.mysqlconnection import connectToMySQL
# TODO import the Ninja class to be used below
from flask_app.models.ninja import Ninja
from pprint import pprint
DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        # TODO Create an instance attribute to hold all ninjas(i.e. a list)
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"    
        return connectToMySQL(DATABASE).query_db(query, data)
        
    #! READ ALL    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( Dojo(dojo) )
        return dojos
    
    #! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return Dojo(result[0])
    
    #! READ ONE WITH MANY
    
    # TODO create a class method to retrive all the ninjas that belong to a certain dojo
    @classmethod
    def get_one_with_ninjas(cls, data):
    # TODO write a join sql query to get a dojo and all its ninjas
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
    # TODO the query will be a list of dictionaries. Each dictionary will contain all the attributes of the dojo and one of the dojo's ninjas.
        pprint(results)
    # TODO create an instance of the dojo class that will have the ninjas attribute. The attribute is a list of all that dojo's ninjas
        dojo = Dojo(results[0])
        print(dojo.name)
    # TODO loop over the list of dictionaries returned from the database.
        for result in results:        
    # TODO create a dictionary to hold and format the ninja's data from each dictionary.
    # TODO append `ninjas.`to the attributes where needed:
            temp_ninja = {
                'id' : result['ninjas.id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'age' : result['age'],
                'dojo_id' : result['dojo_id'],
                'created_at' : result['ninjas.created_at'],
                'updated_at' : result['ninjas.updated_at']
            }
    # TODO once the dictionary is created for each ninjas, append it to the ninjas attribute list. Inside the append method, convert the dictionary created in the previous step to an instance of the ninja class.
            dojo.ninjas.append(Ninja(temp_ninja))
    # TODO finally, return the dojo created above. It will contain the ninjas attribute created in the for loop above.
        return dojo

    #! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name=%(name)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    


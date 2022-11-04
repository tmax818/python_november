from flask_app import flash

class User:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash("first name must be at least 2 characters")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("last name must be at least 2 characters")
        return is_valid
            
        

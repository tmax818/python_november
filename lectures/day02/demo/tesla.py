class Tesla:
    
    all_teslas = []
    CEO = "Elon Musk"
    
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.mileage = 20
        self.under_warranty = True
        Tesla.all_teslas.append(self)
        
    def drive(self, distance):
        self.mileage += distance
        
    def warranty_expires(self, current_year):
        if self.mileage > 100000 or current_year - self.year > 5:
            self.under_warranty = False
    
    
buddys_tesla = Tesla('white', '3', 2022)
tylers_tesla = Tesla('red', 'x', 2015)
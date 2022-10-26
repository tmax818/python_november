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
        
    # def __repr__(self) -> str:
    #     return f"The tesla is {self.color}"
        
    def drive(self, distance):
        self.mileage += distance
        
    def warranty_expires(self, current_year):
        if self.mileage > 100000 or current_year - self.year > 5:
            self.under_warranty = False
            
    @classmethod
    def make_car(cls, color, model, year):
        return Tesla(color, model, year)
        
    @classmethod
    def display_all_teslas(cls):
        for tesla in cls.all_teslas:
            print(tesla)
        
        

        
buddys_tesla = Tesla.make_car('white', '3', 2022)
# buddys_tesla = Tesla('white', '3', 2022)
# tylers_tesla = Tesla('red', 'x', 2015)
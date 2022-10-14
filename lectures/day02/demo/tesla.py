class Tesla:

    CEO = 'Elon Musk'
    all_teslas = []
    stock_price = 277
    
    ## ! Attributes go in the __init__
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        Tesla.all_teslas.append(self)
        print(self)

    ## ! instance methods, things the object does
    def drive(self):
        print(f"The {self.model} is quietly driving down the road...")
    # the model 3 is quietly driving down the road...

    def brake(self):
        print("look out!!!")

    # ! class methods are things the class can do.
    @classmethod
    def display_teslas(cls):
        return cls.all_teslas

    @classmethod
    def set_stock_price(cls, price):
        cls.stock_price = price

    @classmethod
    def make_tesla(cls, model, color, price):
        Tesla(model, color, price)
        cls(model, color, price)

    @staticmethod
    def change_tire(tesla):
        print("I fixed the tire on your {tesla} ")

    
my_tesla = Tesla('model 3', 'red', 1000000)
your_tesla = Tesla('model x', 'black', 1000000)

custom_tesla = Tesla.make_tesla('model s', 'white', 100000000)

Tesla.change_tire(my_tesla)
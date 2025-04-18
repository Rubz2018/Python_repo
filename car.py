class Car:
    # Attributes (Variables) -> These are the characteristics of the object
    color = "Red"
    model = "Toyota"
    year = 2020
    # Methods (Functions)    ->  These are actions that can be performed on the object
    def __init__(self, model, year, color, for_sale):
        # This is a special method(constractor method) that is called when an object is created
        # It is used to initialize the attributes of the class
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    
    def drive(self):
        # This is a method that can be called on an object of the class
        print(f"You drive the {self.model}")
    
    def stop(self):
        print(f"You stopped the {self.model}")
    
    def describe(self):
        print(f"This car is a {self.year} {self.color} {self.model}.It is {self.for_sale} for sale.")
    
    
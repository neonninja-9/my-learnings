class Car:
    def __init__(self, brand , year):
        self.brand = brand
        self.year = year
    def display(self):
        return f"brand is {self.brand} and year is {self.year}"
    
car1 = Car("toyota", 1999)
print(car1.display())


class Car:
    def __init__(self,color):
        self.color = color
    
        
    @classmethod
    def get_price(cls):
        return 'Price was returned'
    
    @staticmethod
    def car_model(year):
        return f'car model is {year}'

print(Car.get_price()) #this willl return sth since class methods does not require instance
print(Car.car_model(1999)) #this willl return sth since static methods does not require instance
# print(Car.color('blue')) # this willl get error since we did not create instance yet
my_car = Car('blue')
print(my_car.color) # s
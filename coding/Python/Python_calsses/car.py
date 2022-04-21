class car:
    def __init__(self,make , model , year):
        self.model = model
        self.make = make
        self.year = year
    
    def descript_car(self):
        car_descriptions = f'{self.make} {self.model} was built on {self.year}'
        return car_descriptions.title()

my_car = car('Audi','A4',2018)
my_car.descript_car()

class Elctric_car(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = 75
    
    def get_battery_info(self):
        """ Get battery info here """
        print(f"Battery Information is {self.battery} KWH")
    

my_tesla_car = Elctric_car('tesla','Model s',2021)
print(my_tesla_car.descript_car())
my_tesla_car.get_battery_info()
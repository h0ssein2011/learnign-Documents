from cmath import pi
from telnetlib import DO


class Dog:
    num_legs = 4 #Class variable
    def __init__(self,name) :
        self.name = name #instance variable

jack = Dog('Jack')
pit = Dog('Pit')

print(jack.name , pit.name)
print(jack.num_legs , pit.num_legs)

jack.num_legs = 6
print(jack.num_legs , pit.num_legs)


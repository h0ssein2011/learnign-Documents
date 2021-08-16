class dog():
    def __init__(self,name, color,breed):
        self.name = name
        self.color = color
        self.breed = breed
    
my_dog = dog(name="mushi" , color="red",breed = 'chinees')
print(my_dog.name)

class circle(object):
    pi = 3.14 

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius *self.radius*self.pi 

my_circle = circle(radius=30)
print(my_circle.area())
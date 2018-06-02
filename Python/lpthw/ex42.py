# Animal is-a object(yes ,sort of confusing) look at the
class Animal (object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self,name):
        ##Animal has-a name
        self.name =name
## Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ##cat has-a name
        self.name=name
##??
class Person(object):
    def __init__(self,name):
        ## Person has-a name
        self.name=name

        ##Person has-a pet of some kind
        self.pet=None

##Employee is-a Person

class Employee(Person):
    def __init__(self,name,salary):
        ## Employee has-a name , salary
        super(Employee,self).__init__(name)
        ##Employee has-a salary
        self.salary=salary

##Fishg is-a boject
class Fish(object):
    pass

##Slmon is a Fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass

##rover is-a dog
rover=Dog("Rover")

##satan is-a cat
satan=Cat("Satan")

##Mary is-a Person
mary=Person("Mary")

##mary has-a pet
mary.pet=satan

##Frank is-a Employee
frank=Employee("Frank")

##Frank has-a rover
frank.pet=rover

##flipper is-a Fish
flipper=Fish()

##crouse is-a Salmon
crouse=Salmon()

harry=Halibut()

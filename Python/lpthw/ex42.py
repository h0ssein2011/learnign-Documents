# Animal is-a object(yes ,sort of confusing) look at the # -*- coding: utf-8 -*-

class Animal (object):
    pass

##?? Dog is a Animal
class Dog(Animal):
    def __init__(self,name):
        ##??
        self.name =name

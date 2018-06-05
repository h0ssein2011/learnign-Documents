class Parent(object):
    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("parent altered()")

class Child(Parent):
    def override(self):
        print("Child override()")

    def altered(self):
        print("Child Before parent altered()")
        super(Child,self).altered()
        print("Child After parent altered()")

dad=Parent()
son=Child()

# this shows that inheret fucntion from parent
dad.implicit()
son.implicit()

# this shows inhert sepretaly
dad.override()
son.override()

# this shows how use super build in fucntion to get paretb
dad.altered()
son.altered()

class Parent(object):
    def override(self):
        print("parent override")
class Child(Parent):
    def override(self):
        print("child override")

Dad=Parent()
Son=Child()

Dad.override()
Son.override()

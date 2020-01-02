class parent(object):
    def implicit(self):
        print("Parent Implicit")

class child (parent):
    pass

dad=parent()
son=child()

dad.implicit()
son.implicit()

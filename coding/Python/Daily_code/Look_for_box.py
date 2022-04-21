
import random
class Look_key():
    def __init__(self,box,location):
        self.box = box
        self.location = random.randint(0,len(box))
        self.key = box[self.location]
    
    def make_a_pile(self):
        pile = [ i for i in self.box]

    def look_for_key(self.box):
        for i in self.box:
            if i == self.key:
                return True
        return False

class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print(self):
        current = self.head
        llstr = ''
        while current:
            llstr += str(current.data)  + '-->'
            current = current.next
        print(llstr)

test = LinkedList()
test.insert_at_begining(1)
test.insert_at_begining(2)
test.insert_at_begining(3)
print(test.print())

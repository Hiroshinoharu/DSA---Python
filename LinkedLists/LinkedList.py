from LinkedLists.Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        pass

    def delete(self, value):
        pass


n1 = Node(3)
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)

ll = LinkedList()
ll.head = n1

n1.next = n2

n2.next = n3

n3.next = n4
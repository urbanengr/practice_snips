class Node:
    """ An object for storing a single node of a linked list.
     Models two attributes - data and the link to the next node in the list"""

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """ an object pointing at the 'head' on a singly linked list."""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """ Returns the number of nodes in the list
         Takes O(n) - linear time """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """ Adds a new node containing data at the head of the list.
         This takes O(1) - constant time """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node



l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
#l.head = N1
print(l.size())

#N2 = Node(20)
#N1.next_node = N2
#print(N1)
#print(N1.next_node)
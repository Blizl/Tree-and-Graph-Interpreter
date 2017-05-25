class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node %s" % data
class Stack:
    def __init__(self):
        self.storage = []
    def peek(self):
        return self.storage[len(self.storage)-1]

    def push(self, data):
       self.storage.append(Node(data)) 
    def pop(self):
        self.storage.pop()
    
node_1 = Node(8)


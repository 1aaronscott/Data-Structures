"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Part 1. Stack implemented using lists


# class Stack:
#     def __init__(self):
#         self.stack = list()
#         self.maxSize = 80
#         self.top = 0

#     def __len__(self):
#         return self.top

#     def push(self, value):
#         if self.top >= self.maxSize:
#             return None
#         self.stack.append(value)
#         self.top += 1
#         return

#     def pop(self):
#         if self.top <= 0:
#             return None
#         item = self.stack.pop()
#         self.top -= 1
#         return item

# Part 2. Stack implemented using LL

class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        ''' get the length of the stack '''
        return self.size

    def push(self, value):
        ''' put a value onto the stack '''
        # create the new node for the value
        new_node = Node(value)
        if not self.head:
            self.size += 1
            self.head = new_node
        else:
            self.size += 1
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def pop(self):
        ''' remove the value at the top of the stack '''
        # if the stack is currently empty
        if self.head == None:
            return None

        # if the stack is not empty
        current = self.head
        old_node = None

        while current.get_next():
            old_node = current
            current = current.get_next()

        if old_node:
            old_node.next_node = None
        else:
            self.head = None

        self.size -= 1
        value = current.get_value()
        return value

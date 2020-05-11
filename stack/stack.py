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

from linked_list_day_1 import LinkedList

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


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def pop(self):
        if self.size >= 1:
            self.size -= 1
            return self.storage.remove_from_head()

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from linked_list_day_1 import LinkedList

# Part 1 implement stack using an array


class Array_Queue:
    ''' Implement using arrays. Mimic an array by having
    a maxSize. '''

    def __init__(self):
        self.queue = list()
        self.maxSize = 80
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        ''' adding to the queue '''
        # Checking if the queue is full
        if self.size() >= self.maxSize:
            return None
        self.queue.append(value)
        self.tail += 1
        return True

    def dequeue(self):
        ''' removing items from queue '''
        # Checking if the queue is empty
        if self.size() <= 0:
            self.resetQueue()
            return None
        data = self.queue[self.head]
        self.head += 1
        return data

    # Calculate size
    def __len__(self):
        return self.tail - self.head

    def size(self):
        return self.tail - self.head

    def resetQueue(self):
        ''' reset the queue '''
        self.tail = 0
        self.head = 0
        self.queue = list()


# Part 2 implementation using a LL
class Queue:
    ''' uses the linked list code from lecture to build a queue '''

    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        ''' adding to the queue '''
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        ''' removing from the queue '''
        if self.storage.head:
            self.size -= 1
            return self.storage.remove_from_head()

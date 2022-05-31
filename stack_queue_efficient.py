from collections import deque

# Double ended queue implementation for stacks and queues, using collections

class Stack():
    def __init__(self):
        self.stack = deque()

    def __repr__(self):
        elements = []

        for element in self.stack:
            elements.append(element)
        
        return " -> ".join(elements)

    def push(self, element):
        self.stack.appendleft(element)

    def pop(self):
        self.stack.popleft()

class Queue():
    def __init__(self):
        self.queue = deque()

     def __repr__(self):
        elements = []

        for element in self.queue:
            elements.append(element)
        
        return " -> ".join(elements)

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.popleft()



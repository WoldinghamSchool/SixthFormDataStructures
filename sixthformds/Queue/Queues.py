from . import abstract_base_

# We wrote this class together in a lesson, remember?
class BaseListQueue(abstract_base_.AbstractQueue):
    def __init__(self, size):
        self.q = []
        self.maxsize = size

    def isFull(self):
        return len(self.q) == self.maxsize

    def isEmpty(self):
        return len(self.q) == 0
    
    def dequeue(self):
        if self.isEmpty():
            print("noooo")
        else:
            return self.q.pop(0)

    def enqueue(self, value):
        if self.isFull():
            print('full')
        else:
            self.q.append(value)
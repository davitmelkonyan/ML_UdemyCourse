# Construct a Queue with two stacks
class Queue2Stacks(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self,elemnet):
        self.inStack.append(elemnet)

    def dequeue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
#!/usr/bin/python
"""
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.
"""
class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minv = []

    def push(self, number):
        # write yout code here
        self.stack += [number]

        if not self.minv or number < self.minv[-1]:
            self.minv += [number]
        else:
            self.minv += [self.minv[-1]]

    def pop(self):
        # pop and return the top item in stack
        if not self.stack:
            return None

        n = self.stack[-1]
        self.stack = self.stack[:-1]
        self.minv = self.minv[:-1]

        return n

    def min(self):
        # return the minimum number in stack
        if not self.minv:
            return None
        
        return self.minv[-1]

if __name__ == '__main__':
    stack = MinStack()    

    stack.push(3)
    stack.push(2)
    stack.push(1)
    print stack.min()
    print stack.pop()
    print stack.min()
    print stack.pop()
    print stack.min()

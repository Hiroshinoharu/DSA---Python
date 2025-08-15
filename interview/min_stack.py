# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if not self.stack:
            return None  # or raise an exception
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]
    
    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

class MaxStack:
    def __init__(self) -> None:
        self.stack = []
        self.max_stack = []
    
    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value > self.max_stack[-1]:
            self.max_stack.append(value)
    
    def pop(self):
        if not self.stack:
            return None  # or raise an exception
        self.max_stack.pop()
        return self.stack.pop()
    
    def getMax(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


obj = MinStack()

obj2 = MaxStack()

obj2.push(2)
obj2.push(0)
obj2.push(3)
print(obj2.getMax())  # Output: 3

obj2.pop()
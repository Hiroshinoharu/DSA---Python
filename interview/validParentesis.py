class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to store the characters
        stack = Stack()

        # Iterate through the characters of the string
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.push(c)
            else:
                # If the stack is empty return false
                if stack.isEmpty():
                    return False
                
                # Check if the character is a closing bracket that matches the top of the stack
                top = stack.pop()
                if (c == ")" and top != "(") or (c == "}" and top != "{") or (c == "]" and top != "["):
                    return False
        
        # If the stack is empty, all brackets are matched
        return stack.isEmpty()
        
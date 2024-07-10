class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Empty stack")
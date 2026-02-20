class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            return -1
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def find(self, value):
        return value in self.stack

    def show(self):
        return self.stack

    def display(self):
        for i in reversed(self.stack):
            print(i)

    def replace(self, old, new):
        for i in range(len(self.stack)):
            if self.stack[i] == old:
                self.stack[i] = new
                return True
        return False

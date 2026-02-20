class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit
        self.dynamic = False

    def push(self, data):
        if not self.dynamic and len(self.stack) >= self.limit:
            return -1
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def prioritize_even(self):
        even = []
        odd = []
        for i in self.stack:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        self.stack = odd + even

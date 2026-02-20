class Queue:
    def __init__(self, limit):
        self.Q = []
        self.limit = limit
        self.front = -1
        self.rear = -1

    def insQueue(self, data):
        if self.rear == self.limit - 1:
            return -1
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.Q.append(data)
        else:
            self.rear += 1
            self.Q.append(data)

    def delQueue(self):
        if self.front == -1 or self.front > self.rear:
            return -1
        value = self.Q[self.front]
        self.front += 1
        return value

    def compress(self):
        if self.front > 0:
            self.Q = self.Q[self.front:self.rear+1]
            self.rear = len(self.Q) - 1
            self.front = 0

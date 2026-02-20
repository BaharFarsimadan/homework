class PriorityCircularQueue(CircularQueue, Stack):

    def __init__(self, limit):
        CircularQueue.__init__(self, limit)
        Stack.__init__(self, limit)

    def enqueue_priority(self, data, priority):
        self.enqueue((priority, data))
        self.sort_queue()

    def sort_queue(self):
        items = []
        while not self.is_empty():
            items.append(self.dequeue())
        items.sort(reverse=True)
        for item in items:
            self.enqueue(item)

    def dequeue_priority(self):
        return self.dequeue()

    def peek(self):
        if self.is_empty():
            return None
        return self.Q[self.front]

    def size(self):
        if self.is_empty():
            return 0
        return (self.rear - self.front + 1) % self.limit

    def clear(self):
        self.front = -1
        self.rear = -1
        self.Q = [None] * self.limit

    def is_full_queue(self):
        return self.is_full()

    def is_empty_queue(self):
        return self.is_empty()

    def display_queue(self):
        self.display()

    def to_list(self):
        result = []
        if self.is_empty():
            return result
        i = self.front
        while True:
            result.append(self.Q[i])
            if i == self.rear:
                break
            i = (i + 1) % self.limit
        return result

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.heapify_up(parent)

    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_val

    def heapify_down(self, i):
        n = len(self.heap)
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

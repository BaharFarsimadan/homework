class Node3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.next = None


class LinkedList3D:
    def __init__(self):
        self.head = None

    def add_first(self, x, y, z):
        new_node = Node3D(x, y, z)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, x, y, z):
        new_node = Node3D(x, y, z)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def search(self, x, y, z):
        cur = self.head
        while cur:
            if cur.x == x and cur.y == y and cur.z == z:
                return True
            cur = cur.next
        return False

    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def print_list(self):
        cur = self.head
        while cur:
            print((cur.x, cur.y, cur.z), end=" -> ")
            cur = cur.next
        print("None")

    def clear(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_first(self):
        if self.head:
            return (self.head.x, self.head.y, self.head.z)

    def get_last(self):
        cur = self.head
        if not cur:
            return None
        while cur.next:
            cur = cur.next
        return (cur.x, cur.y, cur.z)

    def insert_at(self, index, x, y, z):
        if index == 0:
            self.add_first(x, y, z)
            return
        cur = self.head
        for _ in range(index - 1):
            if cur:
                cur = cur.next
        if cur:
            new_node = Node3D(x, y, z)
            new_node.next = cur.next
            cur.next = new_node

    def delete_at(self, index):
        if index == 0 and self.head:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(index - 1):
            if cur:
                cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next

    def update(self, old, new):
        cur = self.head
        while cur:
            if (cur.x, cur.y, cur.z) == old:
                cur.x, cur.y, cur.z = new
                return True
            cur = cur.next
        return False

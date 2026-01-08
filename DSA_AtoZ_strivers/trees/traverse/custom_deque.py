class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # rear
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    # Insert at front
    def append_left(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    # Insert at rear
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    # Remove from front
    def pop_left(self):
        if self.is_empty():
            raise IndexError("pop_left from empty deque")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return data

    # Remove from rear
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return data

    # Peek at front
    def front(self):
        if self.is_empty():
            return None
        return self.head.data

    # Peek at rear
    def rear(self):
        if self.is_empty():
            return None
        return self.tail.data


dq = Deque()
dq.append(10)        # [10]
dq.append(20)        # [10, 20]
dq.append_left(5)    # [5, 10, 20]

print(dq.pop_left()) # 5 → [10, 20]
print(dq.pop())      # 20 → [10]
print(dq.front())    # 10
print(dq.rear())     # 10
print(dq.size())     # 1

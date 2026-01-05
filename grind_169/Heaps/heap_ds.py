'''

| Operation                      | Average / Worst Case | Description           |
| ------------------------------ | -------------------- | --------------------- |
| `push`                         | O(log n)             | Bubble up new element |
| `pop`                          | O(log n)             | Bubble down root      |
| `peek`                         | O(1)                 | Access root           |
| `build_heap` (from n elements) | O(n)                 | Heapify all elements  |


'''


class MinHeap:
    def __init__(self):
        self.heap = []

    # Helper to get parent and child indices
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # 🔹 Insert a new value into heap
    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    # 🔹 Remove and return the smallest element
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()   # Move last to root
        self._heapify_down(0)
        return root

    # 🔹 Peek at smallest element
    def peek(self):
        return self.heap[0] if self.heap else None

    # 🔹 Maintain heap property (heapify_up - insertion)
    def _heapify_up(self, index):
        while index > 0:
            p = self.parent(index)
            if self.heap[index] < self.heap[p]:
                self.heap[index], self.heap[p] = self.heap[p], self.heap[index]
                index = p
            else:
                break

    # 🔹 Maintain heap property (heapify_down - deletion)
    def _heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


h = MinHeap()
h.push(10)
h.push(5)
h.push(3)
h.push(8)

print("Heap array:", h.heap)    # [3, 8, 5, 10]
print("Peek:", h.peek())        # 3
print("Pop:", h.pop())          # 3
print("After pop:", h.heap)     # [5, 8, 10]

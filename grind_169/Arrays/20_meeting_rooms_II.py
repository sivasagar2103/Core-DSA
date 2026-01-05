'''
Meeting Rooms II

Q: Find the maximum number of overlapping meetings 
   that's the minimum rooms required.

Key Idea: Min rooms required for all meetings
Pattern: Overlap counting == minimum required rooms

Intuition
1. Two Pointers (Sort + Sweep Line)
- Sort start & end times
- move pointers to count overlaps

Time: O(n log n)
Space: O(n)

Cons:
- Needs two full sorted lists (start, end)
- Can't easily handle dynamic updates (e.g., adding or removing meetings online)

2. Min heap approach (End time tracking)
- Keep track of current meetings end times in a heap.
- Handles dynamic additions

Time: O(nlogn)
Space: O(n)

Sweep line = count overlaps statically
Heap = manage overlaps dynamically.

| Aspect               | Sweep Line     | Min Heap        |
| -------------------- | -------------- | --------------- |
| Concept              | Count overlaps | Track end times |
| Data structures      | Two arrays     | Heap            |
| Dynamic updates      | ❌ No          | ✅ Yes          |
| Implementation       | Simple         | Moderate        |
| Real-time scheduling | ❌             | ✅              |

Minimum rooms = maximum overlapping meetings.

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

def find_minimum_rooms(arr):
    n = len(arr)
    start = sorted(i[0] for i in arr)
    #[0,5,15]
    end = sorted(i[1] for i in arr)
    #[10,20,30]

    i, j = 0, 0
    current = 0
    maxi = 0

    while i < n:
        if start[i] < end[j]:
            current += 1
            i += 1
        else:
            current -= 1
            j += 1
        maxi = max(current, maxi)
    
    return maxi


def find_minimum_rooms_two(arr):
    #using a min heap
    arr.sort(key = lambda x: x[0])

    min_heap = MinHeap()

    for start, end in arr:
        peek = min_heap.peek()
        if peek is not None and start >= peek:
            min_heap.pop()

        min_heap.push(end)

    #length of heap is the result
    return len(min_heap.heap)

#30 -- 10 -- [20, 30]
slots = [[0, 30], [5, 10], [15, 20]]
res = find_minimum_rooms(slots)
print(res)

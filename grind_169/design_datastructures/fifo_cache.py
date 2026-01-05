'''
I. What is Cache?
- Cache is a fast, temporary storage area for frequently
  accessed data and instructions, used to speed up future 
  requests by reducing the need to fetch information from slower main memory.
- The components are capacity, cache hit, cache miss, and latency.
- The hit ratio of a cache describes how often a searched-for item is found.
- The latency of a cache describes how long the cache can return 
  the desired item when there is a hit.

II. Cache Replacement Policies
1. FIFO - First In, First Out:

2. LIFO - Last In, First Out:

3. LRU - Least Recently Used:

4. MRU - Most Recently Used:

5. LFU - Least Frequently Used:

III. Note:
1. Circular Queue

2. Dequeue

3. Double Linked List

'''

#FIFO cache by using array + dict
'''
Cons: Removing the first element requires shifting all elements → O(n)

'''
class FIFOArrDict:
    def __init__(self, capacity):
        self.capacity = capacity
        self.track = []
        self.data = {}

    def get(self, key):
        if key in self.data:
            return self.data[key]
        return -1
    
    def put(self, key, value):
        if key in self.data:
            self.data[key] = value
            return
        
        current_capacity = len(self.track)
        if current_capacity >= self.capacity:
            old_key = self.track[0]
            for i in range(1, current_capacity):
                self.track[i-1] = self.track[i]

            self.track.pop()
            del self.data[old_key]
        
        self.track.append(key)
        self.data[key] = value
    
    def display(self):
        for key in self.data:
            print(f"{key}:{self.data[key]}", end=" ")
        print()

# Example usage
print("FIFO Array + Dict")
fifo = FIFOArrDict(3)
fifo.put(1, "A")
fifo.put(2, "B")
fifo.put(3, "C")
fifo.display()   # 1:A 2:B 3:C

fifo.put(4, "D")  # Evicts 1:A
fifo.display()   # 2:B 3:C 4:D

print(fifo.get(2))  # Output: B
print(fifo.get(1))  # Output: -1

#To optimise update opeation to O(1), need to use DLL
'''

[HEAD] <-> [ ... real nodes ... ] <-> [TAIL]
self.head and self.tail are not real data nodes.
They are just boundaries that simplify insert/remove logic.
This way, we never deal with None pointers at all.

Note:
In regular doubly linked list → last node's .next = None.
In dummy head/tail approach (which we use) → last real node's .next = tail sentinel.
This avoids special cases when adding/removing nodes.

'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        prev = None
        next = None

class FIFOLinkedListDict:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}

        #dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.data:
            return self.data[key].value
        return -1
    
    def put(self, key, value):
        if key in self.data:
            self.data[key].value = value
            return
        
        current_capcity = len(self.data)
        if current_capcity >= self.capacity:
            oldest = self.head.next #since dummy, we used next
            self._remove(oldest)
            del self.data[oldest.key]
        
        node = Node(key, value)
        self.data[key] = node
        self._add_last(node)

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _add_last(self, node):
        '''
        When we insert a new node at the end, it should sit before the tail sentinel.
        So its next must point to self.tail.
        self.tail.prev always points to the last real node.
        
        '''
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
    
    def display(self):
        curr = self.head.next
        while curr != self.tail:
             print(f"{curr.key}:{curr.value}", end=" ")
             curr = curr.next
        print()

print("FIFO DLL + Dict Demo:")
fifo = FIFOLinkedListDict(3)
fifo.put(1, "A")
fifo.put(2, "B")
fifo.put(3, "C")
fifo.display()   # 1:A 2:B 3:C
fifo.put(4, "D") # Evicts 1
fifo.display()   # 2:B 3:C 4:D

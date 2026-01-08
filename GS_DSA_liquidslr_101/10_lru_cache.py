'''
Problem Statement:
Design and implement a Least Recently Used (LRU) Cache that supports 
the following operations in O(1) time:
- get(key): Return the value of the key if it exists in the cache; otherwise return -1.
- put(key, value): Insert or update the value of the key. 
  If the cache exceeds its capacity, evict the least recently used key.
- The cache must automatically update usage order on every access or update.


Approach Used:
- DLL + Hashmap
- DLL -> Maintain usage order and O(1) time for get and put operations
  . Head : LRU
  . Tail : MRU
- Hashmap: provides fast access to cache entries by key.

Core Idea:
- Every cache entry is stored as a node in a doubly linked list.
- On every get or put operation:
  . accessed node is removed and then added at the tail
- When the cache exceeds capacity,
  . The node right after the head is removed
  . Its corresponding key is deleted from the hashmap

Time: Get -> O(1) ; put -> O(1)
Space: O(capacity)

'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}

        self.head = Node(0, 0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def add_last(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            self.remove(node)
            self.add_last(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.data:
            self.remove(self.data[key])
        
        node = Node(key, value)
        self.data[key] = node
        self.add_last(node)

        current_capacity = len(self.data)
        if current_capacity > self.capacity:
            #first node  --> least accessed one
            head_node = self.head.next
            self.remove(head_node)
            del self.data[head_node.key]
    
    def display(self):
        curr = self.head.next
        while curr != self.tail:
            print(f"{curr.key}:{curr.value}", end=" ")
            curr = curr.next
        print()
        

lru = LRUCache(3)
lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")
lru.display()    # 1:A 2:B 3:C
lru.get(2)       # Access 2 → becomes most recent
lru.display()    # 1:A 3:C 2:B
lru.put(4, "D")  # Evicts 1 (least recently used)
lru.display()    # 3:C 2:B 4:D

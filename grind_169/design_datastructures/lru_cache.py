'''

- Least Recently Used Node will be available at head.
- That means, for every get or update operation, we move the
  accessed node to the tail. [remove and add_last]

DLL + HashMap

'''
#DLL
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
    
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _add_last(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            self._remove(node)
            self._add_last(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.data:
            self._remove(self.data[key])
        
        node = Node(key, value)
        self.data[key] = node
        self._add_last(node)

        current_capacity = len(self.data)
        if current_capacity > self.capacity:
            #first node  --> least accessed one
            head_node = self.head.next
            self._remove(head_node)
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

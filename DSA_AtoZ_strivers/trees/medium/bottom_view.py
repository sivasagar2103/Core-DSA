'''
Steps:
- run a BFS keeping track of x (horizontal distance from root).
- For each x, you only store the last node encountered.
- Track min_x and max_x to avoid sorting dictionary keys.
- Finally, collect nodes from min_x to max_x.

Time: O(N)
Space: O(W)

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.arr = []
    
    def enqueue(self, val):
        self.arr.append(val)
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.arr.pop(0)
    

def bottom_view(root):
    queue = Queue()
    queue.enqueue((root, 0))
    nodes_map = {}
    min_x, max_x = 0, 0
    result = []

    while not queue.is_empty():
        node, x = queue.dequeue()
        
        nodes_map[x] = node.data
        
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        
        if node.left:
            queue.enqueue((node.left, x-1))
        if node.right:
            queue.enqueue((node.right, x+1))

    print(nodes_map)
    for i in range(min_x, max_x+1):
        result.append(nodes_map[i])
    
    return result

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

result = bottom_view(root)
print(result)
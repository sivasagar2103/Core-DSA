'''
BFS + coordinates: 
Time: O(N)	
Space: O(W + H)	+ Uses extra y_map
- Uses y coordinate as unique

Level-order BFS:
Time: O(N)
Space: O(W)
Simplest & fastest
Uses 0 for left and len(level) -1 for right of that particular level

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
        
    def size(self):
        return len(self.arr)


def left_view_by_vertices(root):
    queue = Queue()
    queue.enqueue((root, 0, 0)) #y coordinate, horizontal line
    y_map = {}
    result = []
    min_y, max_y = 0,0

    while not queue.is_empty():
        node, x, y = queue.dequeue()

        if y not in y_map:
            y_map[y] = node.data
        
        max_y = max(max_y, y)
        
        if node.left:
            queue.enqueue((node.left, x-1, y+1))
        if node.right:
            queue.enqueue((node.right, x+1, y+1))
    
    for y in range(min_y, max_y+1):
        result.append(y_map[y])
    
    return result

def left_view_by_level_order(root):
    queue = Queue()
    queue.enqueue(root)
    result = []

    while not queue.is_empty():
        for i in range(queue.size()):
            node = queue.dequeue()
            if i == 0:
                result.append(node.data)
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
    
    return result


def right_view_by_vertices(root):
    queue = Queue()
    queue.enqueue((root, 0, 0)) #y coordinate, horizontal line
    y_map = {}
    result = []
    min_y, max_y = 0,0

    while not queue.is_empty():
        node, x, y = queue.dequeue()

        
        y_map[y] = node.data
        
        max_y = max(max_y, y)
        
        if node.left:
            queue.enqueue((node.left, x-1, y+1))
        if node.right:
            queue.enqueue((node.right, x+1, y+1))
    
    for y in range(min_y, max_y+1):
        result.append(y_map[y])
    
    return result

def right_view_by_level_order(root):
    queue = Queue()
    queue.enqueue(root)
    result = []

    while not queue.is_empty():
        q_size = queue.size()
        for i in range(q_size):
            node = queue.dequeue()
            if i == q_size-1:
                result.append(node.data)
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
    
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


lres1 = left_view_by_vertices(root)
print('left_view_by_vertices: ',lres1)

lres = left_view_by_level_order(root)
print('left_view_by_level_order: ',lres)

rres1 = right_view_by_vertices(root)
print('right_view_by_vertices: ',rres1)

rres = right_view_by_level_order(root)
print('right_view_by_level_order: ', rres)
'''

Top View:
- first node at each HD (leftmost/topmost from each column).

Bottom View:
-  last node at each HD (bottom-most from each column).

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#custom Queue class using list
class Queue:
    def __init__(self):
        self.arr = []
    

    #add the element at rear
    def enqueue(self, value):
        self.arr.append(value)

    #remove from front
    def dequeue(self):
        if not self.is_empty():
            return self.arr.pop(0)
    

    def is_empty(self):
        return len(self.arr) == 0


def insert(root, key):
    if root is None:
        return Node(key)
    
    que = Queue()
    que.enqueue(root)

    while not que.is_empty():
        temp = que.dequeue()

        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            que.enqueue(temp.left)
        
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            que.enqueue(temp.right)
 
    return root

def bottom_view_bfs(root):
    #Group nodes that fall on the same vertical line,
    #BFS will get the last nodes
    #Always overwrite hd map

    queue = Queue()
    queue.enqueue((root, 0))

    hd_map = {} #horizontal distance map

    while not queue.is_empty():
        node, hd = queue.dequeue()

        hd_map[hd] = node.data

        if node.left:
            queue.enqueue((node.left, hd-1))
        if node.right:
            queue.enqueue((node.right, hd+1))
    
    res = []
    for i in sorted(hd_map.keys()):
        res.append(hd_map[i])
    return res

def top_view_bfs(root):
    queue = Queue()
    queue.enqueue((root, 0))

    hd_map = {} #horizontal distance map

    while not queue.is_empty():
        node, hd = queue.dequeue()

        if hd not in hd_map:
            hd_map[hd] = node.data

        if node.left:
            queue.enqueue((node.left, hd-1))
        if node.right:
            queue.enqueue((node.right, hd+1))
    
    res = []
    for i in sorted(hd_map.keys()):
        res.append(hd_map[i])
    return res



root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

top = top_view_bfs(root)
print(top)

bottom = bottom_view_bfs(root)
print(bottom)
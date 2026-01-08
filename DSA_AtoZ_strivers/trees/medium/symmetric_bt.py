'''
mirror image == original tree


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



def symmetric_bfs(root):
    queue = Queue()
    queue.enqueue((root.left, root.right))

    while not queue.is_empty():
        ln, rn = queue.dequeue()

        if not ln and not rn:
            continue
        if not ln or not rn:
            return False
        if ln.data != rn.data:
            return False
        
        queue.enqueue((ln.left, rn.right))
        queue.enqueue((ln.right, rn.left))
    
    return True


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(3)
# root.left.right.right = Node(6)
# root.left.right.right.right = Node(7)

res = symmetric_bfs(root)
print(res)
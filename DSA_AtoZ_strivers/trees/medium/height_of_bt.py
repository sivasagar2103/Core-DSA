'''
- height of a binary tree : No.of nodes
- longest path from the root to a leaf.

Height of a Node:
- Number of edges on the longest path from that node down to a leaf.
- Height of a tree: Height of the root node.
- Leaf Node: Height = 0

Depth of a Node:
- Number of edges from the root to that node.
- Root Node: Depth = 0
- Depth increases as you move down each level.

Height: distance downwards to a leaf.
Depth : distance upwards to the root.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height_of_bt(root):
    #using stack DFS
    stack = [(root, 1)]
    maxi = 0

    while stack:

        node, height = stack.pop()
        maxi = max(height, maxi)
        if node.right:
            stack.append((node.right, height+1))
        if node.left:
            stack.append((node.left, height+1))

    return maxi

class Queue:
    def __init__(self):
        self.arr = []
    
    def enqueue(self, node):
        self.arr.append(node)
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def front(self):
        #0th index element -- old element
        return self.arr.pop(0)
    
    def rear(self):
        #n-1 th index element -- latest element
        return self.arr.pop(-1)
    
    def dequeue(self):
        if not self.is_empty():
            return self.arr.pop(0)
    
    def size(self):
        return len(self.arr)


def find_height_bfs(root):
    queue = Queue()
    queue.enqueue(root)
    maxi = 0

    while not queue.is_empty():
        queue_size = queue.size()
        for i in range(queue_size):
            front = queue.dequeue()
            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        maxi += 1

    return maxi

 
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left= n6

res = find_height_bfs(n1)
print(res)
res1 = height_of_bt(n1)
print(res1)
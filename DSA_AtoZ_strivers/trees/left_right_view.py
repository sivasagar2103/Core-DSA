'''

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


def left_view_bfs(root):
    res = []

    que = Queue()
    que.enqueue(root)

    while not que.is_empty():
        level_length = len(que.arr)

        for i in range(level_length):
            node = que.dequeue()

            if i == 0:
                res.append(node.data)
            
            if node.left:
                que.enqueue(node.left)
            if node.right:
                 que.enqueue(node.right)
    
    return res

def right_view_bfs(root):
    res = []
    que = Queue()
    que.enqueue(root)

    while not que.is_empty():
        level = len(que.arr)

        for i in range(level):
            node = que.dequeue()

            if i == level-1:
                res.append(node.data)
            

            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)
    
    return res


# Build tree manually
root = Node(1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)

left = left_view_bfs(root)
print(left)
#[1, 2, 4]

right = right_view_bfs(root)
print(right)
#[1, 3, 4]


#Node 4 appears in both views because at its level (level 2), it is the only node.

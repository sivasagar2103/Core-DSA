'''
Zig-Zag Traversal

left-to-right and right-to-left of each level.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

def zig_zag(root):
    result = []

    queue = Queue()
    queue.enqueue(root)

    l_to_r = True

    while not queue.is_empty():
        size = queue.size()
        temp = [0] * size
        for i in range(size):
            node = queue.dequeue() #front
            index = i if l_to_r else (size-1-i)
            temp[index] = node.data

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
    
        l_to_r = False if l_to_r else True
        result.append(temp)
    
    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = zig_zag(root)
print(res)
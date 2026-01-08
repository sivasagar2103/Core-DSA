'''

Vertical Traversal of Nodes


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

def vertical_traversal_without_sort(root):
    queue = Queue()
    queue.enqueue((root, (0, 0)))
    nodes_map = {}
    min_x, max_x = 0, 0

    while not queue.is_empty():
        node, (x,y) = queue.dequeue()

        if x not in nodes_map:
            nodes_map[x] = []
        nodes_map[x].append((y, node.data))

        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

        if node.left:
            queue.enqueue((node.left, (x-1, y+1)))
        if node.right:
            queue.enqueue((node.right, (x+1, y+1)))

    result = []
    for x in range(min_x, max_x+1):
        result.append([val for _, val in nodes_map[x]])
    return result


def vertical_traversal(root):
    '''
    Time: O(nlogn)
    Space: O(n)
    '''
    queue = Queue()
    queue.enqueue((root, (0, 0)))

    nodes_map = {}

    while not queue.is_empty():

        node, (x,y) = queue.dequeue()

        if x not in nodes_map:
            nodes_map[x] = []
        nodes_map[x].append((y, node.data))

        if node.left:
            queue.enqueue((node.left, (x-1, y+1)))
        if node.right:
            queue.enqueue((node.right, (x+1, y+1)))

    result = []
    for x in sorted(nodes_map.keys()):
        column = sorted(nodes_map[x], key=lambda k: (k[0], k[1]))
        result.append([val for _, val in column])

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

result = vertical_traversal_without_sort(root)
print(result)

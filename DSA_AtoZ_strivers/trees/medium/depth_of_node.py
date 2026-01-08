class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def depth_of_node(root, target):
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()

        if node is target:
            return depth

        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth+1))
    return -1


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

res = depth_of_node(n1, n5)
print(res)
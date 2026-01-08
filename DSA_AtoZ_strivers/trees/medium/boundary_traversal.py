'''

Boundary Traversal:
Visiting the boundary nodes from root in anti-clock wise direction.

Left Boundary:
- Start from the root and move to the left child if unavailable move to right child,
  continue till leaf node.

Bottom Boundary:
- Traverse the leaf nodes using a preorder traversal
- If node.left is None and node.right is None, add that node to result.

Right Boundary:
- Start from the root and move to the right is unavailable move to left child,
  continue till leaf node.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_leaf(node):
    return not node.left and not node.right

def left_boundary(node, res):
    current = node.left
    while current:
        if not is_leaf(current):
            res.append(current.data)
        if current.left:
            current = current.left
        else:
            current = current.right

def left_boundary_rec(node, res):
    if node and not is_leaf(node):
        res.append(node.data)
        if node.left:
            left_boundary_rec(node.left, res)
        else:
            left_boundary_rec(node.right, res)

def right_boundary(node, res):
    current = node.right
    temp = []
    while current:
        if not is_leaf(current):
            temp.append(current.data)
        if current.right:
            current = current.right
        else:
            current = current.left
    for i in range(len(temp)-1, -1, -1):
        res.append(temp[i])

def right_boundary_rec(node, res):
    '''
    temp array and current variables memory is optimised
    
    '''
    if node and not is_leaf(node):
        if node.right:
            right_boundary_rec(node, res)
        else:
            right_boundary_rec(node, res)
        res.append(node.data) #after recursion reverse order

def bottom_boundary(node, res):
    if is_leaf(node):
        res.append(node.data)
    if node.left:
        bottom_boundary(node.left, res)
    if node.right:
        bottom_boundary(node.right, res)

def boundary_traversal(root):

    res = []
    if not is_leaf(root):
        res.append(root.data)
    
    left_boundary(root, res)
    bottom_boundary(root,res)
    right_boundary(root, res)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = boundary_traversal(root)
print(res)
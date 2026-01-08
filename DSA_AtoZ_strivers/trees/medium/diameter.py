'''
Diameter: 
longest distance btw any nodes of that tree.
or
longest horizontal distance of the tree.
The path may or may not pass through the root.

Diameter = 1 (include curving point) + ht of left st + height of right st

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_diameter_iter(root):
    '''
    explicit stack (iterative postorder traversal + dict for heights)
    Time: O(N), Space: O(h) + O(N)

    '''
    diameter = 0
    stack = [(root, False)]
    heights = {}

    while stack:
        node, visited = stack.pop()

        if not node:
            continue

        if visited:

            left_ht = heights.get(node.left, 0)
            right_ht = heights.get(node.right, 0)

            diameter = max(diameter, (left_ht + right_ht))

            heights[node] = 1 + max(left_ht, right_ht)
        
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
    
    return diameter

def find_diamater_rec(root):
    '''
    recursive DFS (call stack handles traversal + diameter via mutable list)
    taken diameter as list to handler local varible issue
    primitive types are immutable
    Time: O(N), Space: O(h)

    '''
    diameter = [0] #mutable container

    def get_height(node):
        if not node:
            return 0
        
        left = get_height(node.left)
        right = get_height(node.right)

        diameter[0] = max(diameter[0], left+right)

        return 1 + max(left, right)

    get_height(root)
    return diameter[0]


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

res = find_diamater_rec(n1)
print(res)
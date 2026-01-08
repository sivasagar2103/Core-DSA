'''
Balanced Tree:

|Height of a left tree - Height of binary tree| = 1

Top-down --> Preorder traversal
process parent first, then children

Bottom-up --> Postorder traversal
process children first, then parent

Use Top-Down when the answer depends on root-to-leaf path info.
Use Bottom-Up when the answer depends on combining child results.

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def check_balanced_binary_tree(root):
    #find height for every node in left and right
    #and check the difference if >1 return False
    #by using explicit stack and dict
    #Time: O(N), Space: stack: O(h), dict: O(n)
    #post order -- bottom-up

    stack = [(root, False)] #node and visited
    heights = {} #store heights

    while stack:
        node, visited = stack.pop()

        if not node:
            continue

        if visited:
            left = heights.get(node.left, 0)
            right = heights.get(node.right, 0)

            if abs(left-right) > 1:
                return False

            heights[node] = 1 + max(left, right)

        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))


    return True

def check_balanced_bt_rec(root):
    '''
    Bottom-Up approach : post order traversal
    Time: O(N), Space: O(h)

    '''
    if not root:
        return 0
    
    left_ht = check_balanced_bt_rec(root.left)
    right_ht = check_balanced_bt_rec(root.right)

    if abs(left_ht - right_ht) > 1:
        return False

    return 1 + max(left_ht, right_ht)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
# root.left.right.right.right = Node(7)

res = check_balanced_bt_rec(root)
print(res)
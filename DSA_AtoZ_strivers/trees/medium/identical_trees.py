
'''

Two trees are said to be identical if,
- value of node in first tree is equal to the corresponding value of node in second tree.
- left subtree is identical to the corresponding left subtree
- right subtree is identical to the corresponding right subtree

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identical_trees_iter(r1, r2):
    s1 = [r1]
    s2 = [r2]

    while s1 and s2:
        n1 = s1.pop()
        n2 = s2.pop()

        if n1.data != n2.data:
            return False
        
        if n1.right and n2.right:
            s1.append(n1.right)
            s2.append(n2.right)
        elif n1.right or n2.right:
            return False
        
        if n1.left and n2.left:
            s1.append(n1.left)
            s2.append(n2.left)
        elif n1.left or n2.left:
            return False
    
    return not s1 and not s2

def identical_trees_rec(r1, r2):
    #Both None
    if not r1 and not r2:
        return True
    
    #any True
    if not r1 or not r2:
        return False
    
    return (r1.data == r2.data and 
            identical_trees_rec(r1.left, r2.left) and 
            identical_trees_rec(r1.right, r2.right))


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
#root2.left.right = Node(5)

res = identical_trees_iter(root1, root2)
print(res)

res1 = identical_trees_rec(root1, root2)
print(res1)
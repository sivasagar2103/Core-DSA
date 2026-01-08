# ------------------------
# Binary Tree Node
# ------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ------------------------
# DFS Recursive Traversals
# ------------------------

def preorder_recursive(root):
    """Root -> Left -> Right"""
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.data)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


def inorder_recursive(root):
    """Left -> Root -> Right"""
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.data)
        dfs(node.right)
    dfs(root)
    return result


def postorder_recursive(root):
    """Left -> Right -> Root"""
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.data)
    dfs(root)
    return result


# ------------------------
# DFS Iterative Traversals (Stack-based)
# ------------------------

def preorder_iterative(root):
    """Root -> Left -> Right"""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_iterative(root):
    """Left -> Root -> Right"""
    result = []
    stack = []
    current = root #last left will store here
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
    return result


def postorder_iterative_two_stacks(root):
    """Left -> Right -> Root (using 2 stacks)"""
    if not root:
        return []
    result = []
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        result.append(stack2.pop().data)
    return result


def postorder_iterative_one_stack(root):
    """Left -> Right -> Root (using 1 stack)"""
    if not root:
        return []
    result = []
    stack = []
    last_visited = None
    current = root #save the last left
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                result.append(peek.data)
                last_visited = stack.pop()
    return result

# ------------------------
# BFS Iterative Traversals (Queue-based)
# ------------------------

class Queue:
    def __init__(self):
        self.arr = []
    
    def enqueue(self, node):
        self.arr.append(node)
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.arr.pop(0)

def bfs(root):
    queue = Queue()
    queue.enqueue(root)
    result = []
    
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.data)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    
    return result
    

# ------------------------
# Example Usage
# ------------------------

if __name__ == "__main__":
    # Build sample tree
    """
            1
          /   \
         2     3
        / \     \
       4   5     6
    """
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
    n3.right = n6

    print("Preorder Recursive :", preorder_recursive(n1))
    print("Inorder Recursive  :", inorder_recursive(n1))
    print("Postorder Recursive:", postorder_recursive(n1))

    print("Preorder Iterative :", preorder_iterative(n1))
    print("Inorder Iterative  :", inorder_iterative(n1))
    print("Postorder Iterative (2 stacks):", postorder_iterative_two_stacks(n1))
    print("Postorder Iterative (1 stack) :", postorder_iterative_one_stack(n1))

    print("Level Order Traversal by using BFS:", bfs(n1))

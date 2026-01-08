'''

Binary Tree:
root, children, leaf node
Ancestors: Parents are ancestors

Types: 
- Full Binary Tree: Every node should contain zero or 2 children
- Complete BT: All levels should filled except last level. 
  The last level should filled from left.
- Perfect BT: All leaf nodes are at same level.
- Balanced BT: height of tree at maximum logN [No.of nodes]

Representation:
- Each Node stores the data, left pointer and right pointer
- Nodes are manually connected to form the tree structure.
- For leaf nodes left and right are None.

Traversal of Tree:
- Traverse a tree by using BFS or DFS
- DFS is again classified into 3 types
Inorder: left - root - right
Preorder: root - left - right
Postorder: left - right - root

- BFS : traverse level wise


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


'''
       1
     /   \
    2     3
   /
  4

- insertion need to perform by using BFS or Level Order
- we want to insert 5.
- Queue initially: [1]
a. First Iteration:
  - temp = dequeue() → temp = 1
  - if temp.left is None → False (1 has left child 2)
    queue.enqueue(temp.left) → add 2
  - if temp.right is None → False (1 has right child 3)
    queue.enqueue(temp.right) → add 3
  - Queue now: [2, 3]
b. Second Iteration:
   - temp = dequeue() → temp = 2
   - if temp.left is None → False (2 has left child 4)
     queue.enqueue(temp.left) → add 4
   - if temp.right is None → True
     temp.right = Node(5)
     break
- dequeue() let us get to node 2 in order
- We inserted 5 in the correct level-order spot

'''
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

#inorder traversal using recursion stack [DFS]
def inorder_dfs(root):
    res = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        res.append(node.data)
        traverse(node.right)
    
    traverse(root)
    return res

#level wise by using dequeue [BFS]
def bfs_traverse(root):
    que = Queue()
    que.enqueue(root)

    result = []

    while not que.is_empty():
        current = que.dequeue()
        result.append(current.data)

        if current.left:
            que.enqueue(current.left)
        if current.right:
            que.enqueue(current.right)
    
    return result


#search in Binary Tree using DFS
def search_in_bt(root, key):
    if root is None:
        return
    if root.data == key:
        return True
    return search_in_bt(root.left, key) or search_in_bt(root.right, key)

#height of a binary tree
def find_height_of_bt(root):
    if root is None:
        return 0
    return 1 + max(find_height_of_bt(root.left), find_height_of_bt(root.right))

#Count Total Nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

#count leaf Nodes
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)
    


# Build tree manually
root = Node(1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)

inorder_trav = inorder_dfs(root)
print(inorder_trav)
#[4, 2, 1, 3]
res = bfs_traverse(root)
print(res)
search = search_in_bt(root, 3)
print(search)
height = find_height_of_bt(root)
print(height)
count = count_nodes(root)
print(count)
leaf = count_leaf_nodes(root)
print(leaf)

        


            











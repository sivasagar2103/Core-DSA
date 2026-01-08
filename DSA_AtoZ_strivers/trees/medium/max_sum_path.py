class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_max_sum(root):
    '''
    Iterative Postorder (Explicit Stack + Dict)
    sums[node] stores the max one-side gain (node + best child).
    At each node, check node + left + right to possibly update the global maximum.
    
    Time: O(N), Space: O(h) + O(n)
    
    '''
    maxi = 0
    stack = [(root, False)]
    sums = {}

    while stack:
        node, visited = stack.pop()

        if not node:
            continue

        if visited:
            left = sums.get(node.left, 0)
            right = sums.get(node.right, 0)

            maxi = max(maxi, node.data + left + right)

            sums[node] = node.data + max(left, right)

        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return maxi

def find_max_sum_rec(root):
    '''
    Recursive DFS
    Each call:
        - Compute max path through children.
        - Update global maxi
        - Return best one [ node + max(left, right)) ] for parent.
    Time: O(N), Space: O(h)
    
    '''
    maxi = [0]

    def dfs(node):

        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        maxi[0] = node.data + left+ right
        return node.data + max(left, right)
    

    dfs(root)
    return maxi[0]


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

res = find_max_sum_rec(n1)
print(res)
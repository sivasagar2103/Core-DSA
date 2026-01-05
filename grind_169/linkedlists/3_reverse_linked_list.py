'''

prev, curr, next_node

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_ll(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev #last node or tail


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = reverse_ll(n1)
print(res.data)
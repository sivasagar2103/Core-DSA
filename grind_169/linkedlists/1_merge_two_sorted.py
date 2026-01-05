'''

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_sorted(l1, l2):
    dummy_node = Node(0)
    dummy = dummy_node

    while l1 and l2:
        if l1.data <= l2.data:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    
    if l1:
        dummy.next = l1
    if l2:
        dummy.next = l2
    
    return dummy_node.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(4)

m1 = Node(1)
m2 = Node(3)
m3 = Node(4)

n1.next = n2
n2.next = n3

m1.next = m2
m2.next = m3

res = merge_two_sorted(n1, m1)
print(res.data)

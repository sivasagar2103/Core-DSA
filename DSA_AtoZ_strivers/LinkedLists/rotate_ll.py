class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None


def rotate_ll(head, k):
    n = 1
    tail = head
    while tail.next:
        n += 1
        tail = tail.next
    
    new_tail = head
    for _ in range(n-k-1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    
    new_tail.next = None
    tail.next = head

    return new_head


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

k = 2
res = rotate_ll(a1, k)

temp = res
while temp is not None:
    print(temp.data)
    temp = temp.next
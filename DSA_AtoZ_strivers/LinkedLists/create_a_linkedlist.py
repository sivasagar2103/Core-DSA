class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(2)
b = Node(4)
c = Node(5)
d = Node(6)
a.next = b
b.next = c
c.next = d

head = a
ll_length = 0
while head:
    print(head.data)
    ll_length += 1
    head = head.next

print('ll_length:',ll_length)

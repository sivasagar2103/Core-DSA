'''

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def odd_even(head):
    pass

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

res = odd_even(n1)
while res:
    print(res.data, end=" -> ")
    res = res.next
print()

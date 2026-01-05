'''

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_numbers(h1, h2):
    carry = 0
    dummy_node = Node(0)
    dummy = dummy_node

    while h1 or h2 or carry:
        a = h1.data if h1 else 0
        b = h2.data if h2 else 0

        total = a + b + carry
        dig = total % 10
        carry = total //10

        dummy.next = Node(dig)
        dummy = dummy.next

        if h1:
            h1 = h1.next
        if h2:
            h2 = h2.next
    
    return dummy_node.next

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

n1 = Node(2)
n2 = Node(4)
n3 = Node(3)

n1.next = n2
n2.next = n3

m1 = Node(5)
m2 = Node(6)
m3 = Node(4)

m1.next = m2
m2.next = m3

res = add_numbers(n1, m1)
while res:
    print(res.data, end=" -> ")
    res = res.next
print()


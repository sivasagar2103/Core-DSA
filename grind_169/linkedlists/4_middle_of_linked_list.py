'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middle_of_ll(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = middle_of_ll(n1)
print(res.data)

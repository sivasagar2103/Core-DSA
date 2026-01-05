'''

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_nth_node_ll(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    #place the fast pointer at n steps
    for i in range(n):
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
n = 2
res = remove_nth_node_ll(n1, n)
while res:
    print(res.data, end=" -> ")
    res = res.next
print()

'''

slow and fast pointers

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


#head = [3,2,0,-4], pos = 1
n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

res = detect_cycle(n1)
print(res)



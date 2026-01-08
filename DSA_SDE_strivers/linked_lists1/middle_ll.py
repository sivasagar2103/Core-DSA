'''
Problem:

Approach:
1. Fast and Slow Pointers



Time: O(N/2)
Space: O(1)

'''

class SingleNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


a = SingleNode(1)
b = SingleNode(3)
c = SingleNode(2)
d = SingleNode(4)

a.next = b
b.next = c
c.next = d

h = find_middle(a)
print_linked_list(h)
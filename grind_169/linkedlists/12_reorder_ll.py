'''
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reorder_list(head):
    if not head or not head.next:
        return head

    # Step 1: Find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second = reverse(slow.next)
    slow.next = None  # cut first half
    first = head

    # Step 3: Merge two halves
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# Helper to print list
def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")


# Example: head = [1,2,3,4]
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

reorder_list(n1)
print_list(n1)  # 1 -> 4 -> 2 -> 3 -> None

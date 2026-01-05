'''
Intution:
- Find middle [slow and fast] -> 
- reverse second half [from slow to tail]
- first = head ; second = middle
- while second
  . compare the values and return True or False
  . first.next, second.next

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second = reverse(slow)
    first = head

    # Step 3: Compare halves
    while second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next

    return True


def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# Example 1: Palindrome [1,2,2,1]
n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
print(is_palindrome(n1))  # True

# Example 2: Not palindrome [1,2]
m1 = Node(1)
m2 = Node(2)
m1.next = m2
print(is_palindrome(m1))  # False

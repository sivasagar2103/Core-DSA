'''
Intuition:
- Merge Sort
- Use the fast & slow pointer to find the middle.
- Recursively sort left and right halves, and merge them.

Time: O(nlogn)
Sapce: O(logn) [recursive space]

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def get_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sort_list(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    right = middle.next
    middle.next = None

    left_sorted = sort_list(head)
    right_sorted = sort_list(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    dummy = Node(0)
    curr = dummy

    while left and right:
        if left.data < right.data:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    curr.next = left or right
    return dummy.next

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

n1 = Node(4)
n2 = Node(2)
n3 = Node(1)
n4 = Node(3)

n1.next = n2
n2.next = n3
n3.next = n4

res = sort_list(n1)
while res:
    print(res.data, end=" -> ")
    res = res.next
print()
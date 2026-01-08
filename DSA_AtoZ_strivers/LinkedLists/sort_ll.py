class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

def sort_ll(head):
    temp = head
    while temp is not None:
        current = temp.next
        while current is not None:
            if current.data < temp.data:
                current.data, temp.data = temp.data, current.data
            current = current.next
        temp = temp.next

def get_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy = Node()
    tail = dummy

    while left and right:
        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        
        tail = tail.next
    
    tail.next = left or right
    return dummy.next


def merge_sort_ll(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    right = mid.next
    mid.next = None

    left_sort = merge_sort_ll(head)
    right_sort = merge_sort_ll(right)

    return merge(left_sort, right_sort)


a1 = Node(4)
a2 = Node(2)
a3 = Node(1)
a4 = Node(3)
a5 = Node(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

res = merge_sort_ll(a1)

temp = res
while temp is not None:
    print(temp.data)
    temp = temp.next
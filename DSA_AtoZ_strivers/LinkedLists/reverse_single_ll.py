class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def convert_array_ll(arr):
    node = Node(arr[0])
    temp = node
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return node

def reverse_ll_using_stack(head):
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next
    return head

def reverse_ll_without_stack(head):
    prev = None
    temp = head

    while temp is not None:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
    
    return prev

def reverse_ll_using_recursion(head):
    #base case
    if head is None or head.next is None:
        return head
    
    new_head = reverse_ll_using_recursion(head.next)

    head.next.next = head
    head.next = None

    return new_head


arr = [1,2,3,4,5]
ll_head = convert_array_ll(arr)
#reverse_ll_head = reverse_ll_using_stack(ll_head)
#rev_ll_head_without_stack = reverse_ll_without_stack(ll_head)
rev_ll_recursion = reverse_ll_using_recursion(ll_head)
temp = rev_ll_recursion
while temp is not None:
    print(temp.data)
    temp = temp.next


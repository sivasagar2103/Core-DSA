'''
Problem:
Given a linked list and an integer N, the task is to delete the Nth node
from the end of the linked list and print the updated linked list.

Approach:
1. Find the total length(L) and delete (L-N+1) the node
- Traverse the entire list to find the total length (L).
- Compute the position to delete from the start: (L - N + 1).
- Traverse again to that position and adjust pointers to remove the node.

Time: O(l) + O(L-N)
Space: O(1)

Note: 
Removing the head node (when N == L).
Removing the tail node (when N == 1).

2. Fast and Slow pointer
- Initialize two pointers, both at the head.
- Advance the fast pointer N nodes ahead of the slow pointer.
- Move both pointers in tandem until the fast pointer reaches the end.
- The slow pointer will then be just before the node to be deleted.
  Adjust pointers to remove the N-th node from end.

Time: O(L)
Space: O(1)

Note:
Deleting the head node (fast pointer reaches NULL after the initial N steps).

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


def remove_nth_node_bf(head, n):
    length = 0
    temp = head

    while temp is not None:
        length += 1
        temp = temp.next

    if length == n:
        return head.next
    
    del_point = length - n

    temp = head
    while temp is not None:
        del_point -= 1
        if del_point == 0:
            break
        temp = temp.next
    
    temp.next = temp.next.next

    return head
   

def remove_nth_node_opt(head, n):
    slow = head
    fast = head

    for i in range(n):
        fast = fast.next
    
    if fast is None:
        return head.next
    
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return head

a = SingleNode(1)
b = SingleNode(2)
c = SingleNode(3)
d = SingleNode(4)
e = SingleNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

n = 2
h = remove_nth_node_opt(a, n)
print_linked_list(h)
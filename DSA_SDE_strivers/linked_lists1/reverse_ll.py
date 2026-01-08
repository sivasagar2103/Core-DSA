'''
Problem:
Given the head of a singly linked list, write a program to reverse the linked list,
and return the head pointer to the reversed list.

Approach:
1. Brute Force
- Traverse the linked list and push all node values/data onto a stack.
- Reset traversal to the list head, and for each node, pop a value from the stack 
  and assign it to the node's data.
- Continue until the entire list is updated in reversed order.

Time: O(2N)
Space: O(N)

2. Three Pointer Approach
- Initialize three pointers: prev: null, current: head, next : null
- Loop through the list. For each node, store the next node,
  set curr->next to prev then advance prev to curr and curr to next.
- Continue until the end of the list. At the end, prev will be the new head.

Time: O(N)
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

def reverse_ll_bf(head):
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


def reverse_ll_opt(head):
    current = head
    prev = None
    after = None

    while current is not None:
        after = current.next

        current.next = prev

        prev = current

        current = after
    
    return prev


a = SingleNode(1)
b = SingleNode(3)
c = SingleNode(2)
d = SingleNode(4)

a.next = b
b.next = c
c.next = d

h = reverse_ll_opt(a)
print_linked_list(h)
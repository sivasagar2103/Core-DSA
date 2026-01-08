'''
Problem:
Given two sorted linked lists, merge them to produce a combined sorted linked list. 
Return the head of the final linked list created.

Approach:
1.  In-Place Merge
- Assign pointers l1 and l2 to the heads of the two lists.
- Ensure l1 starts with the smaller value by comparing and swapping if needed.
- Keep a res pointer to remember the head of the result (it starts at l1).
- Traverse both lists:
  . Move through l1 as long as l1's node value is less than or equal to l2's node value,
    keeping track of the last node visited.
  . When a node in l2 is smaller, connect the previous node (temp) to l2.
  . Swap l1 and l2 so l1 is always the list with the smaller starting node.
- Repeat the process until you reach the end of one list.
- Attach the remainder of the unfinished list to the merged result.

Time: O(N+M)
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


def merge_sort_ll(head1, head2):
    dummy = SingleNode(0)
    temp = dummy

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        
        temp = temp.next
    
    if head1 is not None:
        temp.next = head1
    else:
        temp.next = head2
    
    return dummy.next



a = SingleNode(1)
b = SingleNode(3)
c = SingleNode(5)

a.next = b
b.next = c

d = SingleNode(2)
e = SingleNode(4)
f = SingleNode(6)

d.next = e
e.next = f

res = merge_sort_ll(a, d)
print_linked_list(res)
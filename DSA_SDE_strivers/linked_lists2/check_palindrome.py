'''
Problem:
Check if the given Linked List is Palindrome

Approach:
1. Stack DS
- Traverse the linked list and store node values in a stack or array 
  (which effectively reverses the sequence). Then iterate from the head 
  and compare each node value to the values popped from the stack or read 
  in reverse from the array.

Time: O(N)
Space: O(N)

2. Reverse and Two Pointer
- Use fast and slow pointers to find the middle.
- Reverse the second half of the list in place.
- Compare the two halves node by node.
- (Optionally) Restore the original list structure.

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

def is_palindrome_bf(head):
    temp = head
    stack = []

    while temp is not None:
        stack.append(temp.data)
        temp = temp.next
    
    print(stack)
    temp = head
    while temp is not None:
        #print(stack.pop())
        if temp.data != stack.pop():
            return False

        temp = temp.next

    return True

def reverse_ll(head):
    current = head
    after = None
    prev = None

    while current is not None:
        after = current.next
        current.next = prev
        prev = current
        current = after
    return prev

def is_palindrome_pointers(head):
    slow = head
    fast = head

    if head is None or head.next is None:
        return True

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    new_head = reverse_ll(slow)

    first = head
    second = new_head

    while second is not None:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next

    return True

#LL: 1  2  3  2  1
a = SingleNode(1)
b = SingleNode(2)
c = SingleNode(3)
d = SingleNode(2)
e = SingleNode(1)

a.next = b
b.next = c
c.next = d
d.next = e

res = is_palindrome_pointers(a)
print(res)
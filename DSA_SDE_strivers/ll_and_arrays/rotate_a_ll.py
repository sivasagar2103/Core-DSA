'''
Problem:
Given the head of a linked list, rotate the list to the right by k places.

Approach:
1. Using Circular LL concept
- Calculate List Length: Traverse to count the number of nodes (n).
- Make List Circular: Connect the last node to the head, forming a circular list.
- Use k=k%n since rotating by the list's length returns it to original order.
- Find New Tail: Move (n - k) steps from the head to locate the new tail.
- Break the Circle: Set the next of the new tail to null; the node after becomes the new head.

Time: O(n)
Only two traversals: one for length, one for finding the new tail/head.
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

def rotate_by_k_opt(head, k):
    temp = head
    length = 1

    while temp.next is not None:
        length += 1
        temp = temp.next
    
    temp.next = head
    k = k % length #if k > length
    end = length - k
    while end:
        temp = temp.next
        end -= 1
    head = temp.next #4
    temp.next = None #3 keeping it as a None

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

k = 2

res = rotate_by_k_opt(a, k)
print_linked_list(res)
#Output: head = [4,5,1,2,3]
'''
Problem:
Given the head of a singly linked list of `n` nodes and an integer `k`, 
where k is less than or equal to `n`. Your task is to reverse the order 
of each group of `k` consecutive nodes, if `n` is not divisible by `k`, 
then the last group of remaining nodes should remain unchanged.

Approach:
1. 
- Segment Identification:
  . Start from the head of the linked list and use 
    a helper function to reach the kth node, thus 
    segmenting the list into groups of size k.
- Reverse Each Segment:
  . For every complete segment of k nodes:
    . Temporarily disconnect the segment from the rest of the list.
    . Reverse the segment using the standard three-pointer reversal method.
- Connect Segments:
  . After reversing, reconnect the last node of the previous reversed segment 
    to the head of the new reversed segment.
  . If dealing with the first segment, update the head pointer.
  . Continue with the next segment.
- Handle Remaining Nodes:
  . If the remaining segment has fewer than k nodes,
    leave it as-is and connect it to the last reversed segment.

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

def reverse_sub_ll(head):
    current = head
    after = None
    prev = None
    while current is not None:
        after = current.next
        current.next = prev
        prev = current
        current = after
    return prev



def get_kth_node(temp_head, k):
    k -= 1
    while temp_head is not None and k > 0:
        k -= 1
        temp_head = temp_head.next
    return temp_head

def reverse_ll_k(head, k):
    temp = head

    prev_last = None

    while temp is not None:
        kth_node = get_kth_node(temp, k)

        if kth_node is None:
            if prev_last:
                prev_last.next = temp
            break

        next_node = kth_node.next

        #forming a sub ll
        kth_node.next = None

        reverse_sub_ll(temp)

        # Adjust the head if the reversal
        # starts from the head
        if temp == head:
            head = kth_node
        else:
            prev_last.next = kth_node
        
        prev_last = temp

        temp = next_node
    
    return head

#LL: 1  2  3  4  5  6  7  8  9  10, k = 3
a = SingleNode(1)
b = SingleNode(2)
c = SingleNode(3)
d = SingleNode(4)
e = SingleNode(5)
f = SingleNode(6)
g = SingleNode(7)
h = SingleNode(8)
i = SingleNode(9)
j = SingleNode(10)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j

k = 3

res = reverse_ll_k(a, k)
print_linked_list(res)
#Output: 3  2  1  6  5  4  9  8  7  10

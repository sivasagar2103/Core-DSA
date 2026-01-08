'''
Problem:
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

Approach:
1. Brute Force : Node itself that is the common attribute
- Keep any one of the list to check its node present in the other list.
- Iterate through the other list. Here, it is the first one. 
- Check if the both nodes are the same. If yes, we got our first intersection node.
- If not, continue iteration.
- If we did not find an intersection node, return None

Time:  O(m*n)
Space:  O(1)

2. HashMap
- Iterate through list 1 and hash its node address. 
- Iterate through list 2 and search the hashed value in the hash table.
  If found, return node else return None.

Time: Iterating through list 1 first takes O(n),
      then iterating through list 2 takes O(m). 
Space: O(n)

3. Dummy Nodes
- Take two dummy nodes for each list. Point each to the head of the lists.
- Iterate over them. If anyone becomes null, 
  point them to the head of the opposite lists and 
  continue iterating until they collide.

Time: O(2*max(len(first_ll, second_ll)))
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


def find_intersection_bf(head1, head2):
    while head2 is not None:
        temp = head1
        while temp is not None:
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    return None

def find_intersection_hm(head1, head2):
    hash_map = {}

    while head1 is not None:
        hash_map[head1] = head1.data
        head1 = head1.next
    
    while head2 is not None:
        if head2 in hash_map:
            return head2
        head2 = head2.next
    return None

def find_intersection_dummy(head1, head2):
    d1 = head1
    d2 = head2

    while d1 != d2:
        d1 = head2 if d1 == None else d1.next
        d2 = head1 if d2 == None else d2.next
    
    return d1


a = SingleNode(1)
b = SingleNode(3)
c = SingleNode(1)
d = SingleNode(2)
e = SingleNode(4)


f = SingleNode(3)


a.next = b
b.next = c
c.next = d
d.next = e

f.next = d

res = find_intersection_dummy(a, f)
print(res.data)


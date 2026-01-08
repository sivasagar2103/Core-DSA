'''
Problem:
Detect a Cycle in a Linked List

Approach:
1. HashMap and Traverse
- Traverse the linked list from the head.
- Use a hash map (dictionary) to store nodes already visited.
- For each node, check if it is already in the hash map.
  . If yes, return this node (indicates a cycle).
  . If no, add it to the hash map and continue.
- If you reach the end (None), return None (no cycle).

Time: O(n)
Space: O(n)

2. Fast and Slow : Finding Cycle and return the first element inside the cycle
- Use two pointers: slow (moves one step at a time) and fast (moves two steps at a time).
- Traverse the linked list.
- If the two pointers meet, a cycle exists and return the meeting node.
- If the fast pointer reaches the end (None), no cycle exists, return None.

Time: O(n)
Space: O(1)

3. Floyd's + two-pointer reset : Finding Cycle Entry Point
- First, use Floyd's Tortoise and Hare algorithm to find the meeting point inside the cycle.
- Once slow and fast meet, reset one pointer to head.
- Move both pointers one step at a time until they meet again.
- The meeting point of these two pointers is the start of the cycle.

Time: O(n)
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


def detect_a_cycle_bf(head):
    temp = head
    hash_map = {}

    while temp is not None:
        if temp in hash_map:
            return temp
        hash_map[temp] = temp.data
        temp = temp.next
    return None

def detect_a_cycle_sf(head):
    #To detect a cycle and return a node inside the cycle:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow
      
    return None

def detect_a_intersection_sf(head):
    #To detect a cycle and return the starting node of the cycle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

a = SingleNode(1)
b = SingleNode(2)
c = SingleNode(3)
d = SingleNode(4)
e = SingleNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

res = detect_a_cycle_bf(a)
print(res.data)


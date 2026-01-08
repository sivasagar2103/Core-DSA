class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def detect_cycle_head(head):
    temp = head
    node_value_map = {}
    while temp is not None:
        if temp in node_value_map:
            return temp.data
        node_value_map[temp] = temp.data
        temp = temp.next
    return None
        
def detect_cycle_head_pointers(head):
    #Time: O(n), space: O(1)
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
            return entry.data

    return None

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a3

res = detect_cycle_head_pointers(a1)
print(res)


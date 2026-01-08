class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def detect_cycle_length(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            temp = slow.next
            while temp != fast:
                count += 1
                temp = temp.next
            return count
    
    return 0



a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)

a1.next = a2
a2.next = a5
a3.next = a4
a4.next = a5
a5.next = a2   # <- creates cycle: 5 → 2 → 5 → 2 → ...


res = detect_cycle_length(a1)
print(res)
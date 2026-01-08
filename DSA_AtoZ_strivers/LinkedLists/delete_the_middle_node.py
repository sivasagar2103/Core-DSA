class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
    
def delete_middle_node(head):
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast= fast.next.next
    
    prev.next = slow.next

    return head


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
res = delete_middle_node(a1)
temp = res
while temp is not None:
    print(temp.data)
    temp = temp.next


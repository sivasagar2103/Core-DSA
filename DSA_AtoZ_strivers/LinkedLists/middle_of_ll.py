class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


def find_middle_node_bf(head):
    temp = head
    l = 0

    while temp is not None:
        l +=1
        temp = temp.next
    
    middle = l //2
    mid = middle
    temp = head
    while temp is not None:
        if mid == 0:
            break
        mid -= 1
        temp = temp.next
    return temp.data

def find_middle_pointers(head):
    slow = head
    fast = head

    while fast:
        slow = slow.next
        fast = fast.next.next

    return slow.data

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
res = find_middle_node_bf(a1)
print(res)
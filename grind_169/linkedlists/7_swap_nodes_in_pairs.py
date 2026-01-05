'''

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        #swapping
        prev.next = second
        first.next = second.next
        second.next = first
        
        #move prev and head
        prev = first
        head = first.next
    
    return dummy.next

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = swap_nodes(n1)
while res:
    print(res.data, end=" -> ")
    res = res.next
print()



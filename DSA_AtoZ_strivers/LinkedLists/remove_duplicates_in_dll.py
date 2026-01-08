class NodeDLL:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        self.prev = None


def remove_duplicates_sorted(head):
    temp = head
    while temp and temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head


def remove_duplicates_unsorted(head):
    pass
        

#2O(n) == O(n)
        

# DLL Example
a1 = NodeDLL(5)
a2 = NodeDLL(4)
a3 = NodeDLL(3)
a4 = NodeDLL(3)
a5 = NodeDLL(1)
a6 = NodeDLL(1)

a1.next = a2
a2.prev = a1
a2.next = a3
a3.prev = a2
a3.next = a4
a4.prev = a3
a4.next = a5
a5.prev = a4
a5.next = a6
a6.prev = a5

target = 7

result = remove_duplicates_sorted(a1)
temp = result

while temp is not None:
    print(temp.data)
    temp = temp.next

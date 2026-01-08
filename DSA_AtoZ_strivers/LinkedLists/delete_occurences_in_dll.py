class NodeDLL:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        self.prev = None

def delete_node_dll(head, value):
    dummy = NodeDLL()
    dummy.next = head

    #This if block to handle the empty DLL's
    if head:
        head.prev = dummy

    prev = dummy
    temp = head

    while temp is not None:
        if temp.data == value:
            prev.next = temp.next
            if temp.next:
                temp.next.prev = prev
        else:
            prev = temp
        
        temp = temp.next
    
    new_head = dummy.next

    #This if block disconnect the dummy node to head.
    if new_head:
        new_head.prev = None
    return new_head
        

# DLL Example
a1 = NodeDLL(4)
a2 = NodeDLL(1)
a3 = NodeDLL(3)
a4 = NodeDLL(2)
a5 = NodeDLL(1)
a1.next = a2
a2.prev = a1
a2.next = a3
a3.prev = a2
a3.next = a4
a4.prev = a3
a4.next = a5
a5.prev = a4

res_head = delete_node_dll(a1, 1)

# Print result
temp = res_head
while temp:
    print(temp.data)
    temp = temp.next
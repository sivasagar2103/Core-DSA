class NodeSLL:
    def __init__(self, data = 0):
        self.data = data
        self.next = None


def delete_node_sll(head, value):
    dummy = NodeSLL()
    dummy.next = head
    prev = dummy
    temp = head
    while temp is not None:
        if temp.data == value:
            prev.next = temp.next
        else:
            prev = temp
        
        temp = temp.next

    return dummy.next


a1 = NodeSLL(4)
a2 = NodeSLL(1)
a3 = NodeSLL(3)
a4 = NodeSLL(2)
a5 = NodeSLL(1)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

res_head = delete_node_sll(a1, 1)

# Print result
temp = res_head
while temp:
    print(temp.data)
    temp = temp.next
class Node:
    def __init__(self, data=0):
        self.data = data
        self.prev = None
        self.next = None

def convert_arr_to_dll(arr):
    n = len(arr)
    head = Node(arr[0])
    prev_node = head
    for i in range(1, n):
        current_node = Node(arr[i])
        current_node.prev = prev_node
        prev_node.next = current_node
        prev_node = current_node

    return head

def reverse_dll(head):
    back = None
    current = head

    while current is not None:
        back = current.prev
        current.prev = current.next
        current.next = back
        current = current.prev
    
    return back.prev

def add_two(l1_head, l2_head):
    temp_node = Node()
    temp_head = temp_node
    carry = 0

    while l1_head is not None or l2_head is not None or carry:
        sum = 0
        if l1_head is not None:
            sum += l1_head.data
            l1_head = l1_head.next
        if l2_head is not None:
            sum += l2_head.data
            l2_head = l2_head.next
        sum += carry
        carry = sum // 10
        dig = sum % 10
        temp_head.next = Node(dig)
        temp_head = temp_head.next
    
    return temp_node.next



l1 = [2,4,3]
l2 = [5,6,4]
l1_head = convert_arr_to_dll(l1)
l2_head = convert_arr_to_dll(l2)

result = add_two(l1_head, l2_head)
temp = result

while temp is not None:
    print(temp.data)
    temp = temp.next
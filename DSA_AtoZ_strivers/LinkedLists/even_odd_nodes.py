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

def even_odd_nodes(head):
    even_node = Node()
    temp_even = even_node

    odd_node = Node()
    temp_odd = odd_node

    temp = head
    while temp is not None:
        if temp.data % 2 == 0:
            temp_even.next = Node(temp.data)
            temp_even = temp_even.next
        else:
            temp_odd.next = Node(temp.data)
            temp_odd = temp_odd.next
        temp = temp.next
    
    print(temp_even.data)
    temp_even.next = odd_node.next
    
    return even_node.next
    
def even_odd_indices(head):
    odd = head #pointer 1
    even = odd.next #pointer 2
    even_start = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next
    
    odd.next = even_start

    return head



arr = [1,2,3,4,5,6,7,8]
head = convert_arr_to_dll(arr)
#result = even_odd_nodes(head)
result = even_odd_indices(head)
temp = result

while temp is not None:
    print(temp.data)
    temp = temp.next
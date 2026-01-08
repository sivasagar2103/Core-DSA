class Node:
    def __init__(self, data):
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
    #Time complexity: O(2n) -- for two iteration push and pop
    #space complexity: O(n) -- for stack
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next
    
    temp = head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next

    return head

def reverse_dll_single_iteration(head):
    #Time complexity: O(n)
    #space complexity: O(1)
    #swap the current and next pointers.
    back = None
    current = head

    while current is not None:
        back = current.prev
        current.prev = current.next
        current.next = back
        current = current.prev
    
    return back.prev



arr = [1,2,3,5]
head = convert_arr_to_dll(arr)

#reverse_head = reverse_dll(head)

reverse_head = reverse_dll_single_iteration(head)

temp = reverse_head

while temp is not None:
    print(temp.data)
    temp = temp.next



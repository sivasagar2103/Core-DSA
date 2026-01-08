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

def remove_nth_node_from_last(head, n):
    dummy_node = Node()
    dummy_node.next = head
    slow = fast = dummy_node
    for i in range(n+1):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy_node.next

def remove_nth_node_from_first(head, n):
    #need to implement
    pass

arr = [1,2,3,5]
count = 3
head = convert_arr_to_dll(arr)
delete_head = remove_nth_node_from_last(head, count)
temp = delete_head

while temp is not None:
    print(temp.data)
    temp = temp.next
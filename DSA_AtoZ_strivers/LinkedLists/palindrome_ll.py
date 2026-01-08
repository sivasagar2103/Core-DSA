class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def convert_array_ll(arr):
    node = Node(arr[0])
    temp = node
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return node

def is_palindrome(head):
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next
    
    temp = head
    while temp is not None:
        if temp.data != stack.pop():
            return False
        
        temp = temp.next
    
    return True

def is_palindrome_using_pointers(head):
    #need to implement
    pass


arr = [1,2,3,2,1]
ll_head = convert_array_ll(arr)
res = is_palindrome(ll_head)
print(res)

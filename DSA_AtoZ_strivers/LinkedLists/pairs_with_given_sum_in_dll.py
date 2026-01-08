class NodeDLL:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        self.prev = None


def find_pairs(head, target):
    #brutre force approach with O(n*2) time complexity
    #1,2,4,5,6,8,9
    res = []
    temp = head
    while temp is not None:
        slow = temp
        fast = temp.next
        while fast is not None:
            if target - fast.data == slow.data:
                temp_arr = [slow.data, fast.data]
                res.append(temp_arr)
            fast = fast.next
        temp = temp.next
    print(res)

def find_pairs_two_pointers(head, target):
    '''
    DLL must be sorted.
    left = head, right = tail
    left + right == target : record the pair
    left + right < target: move left forward
    left + right > target: move right backward
    '''
    result = []
    tail = head

    #O(n)
    while tail.next:
        tail = tail.next
    left = head
    right = tail

    #O(n)
    while left and right and left != right and left.prev != right:
        current_sum = left.data + right.data
        if current_sum == target:
            pair = [left.data, right.data]
            result.append(pair)

            #To get unique pairs
            l_value = left.data
            r_value = right.data

            while left and left.data == l_value:
                left = left.next
            while right and right.data == r_value:
                right = right.prev

        elif current_sum < target:
            left = left.next
        elif current_sum > target:
            right= right.prev
    
    return result

#2O(n) == O(n)
        

# DLL Example
a1 = NodeDLL(1)
a2 = NodeDLL(2)
a3 = NodeDLL(4)
a4 = NodeDLL(5)
a5 = NodeDLL(6)
a6 = NodeDLL(8)
a7 = NodeDLL(9)

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
a6.next = a7
a7.prev = a6

target = 7

result = find_pairs_two_pointers(a1, target)
print(result)

'''
Problem:
Given the heads of two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Approach:
1. DummyNode
- Create a dummy node and set a carry to 0.
- Loop through both lists:
  . sum = (value from list 1) + (value from list 2) + carry
  . carry = sum // 10
  . result node value = sum % 10
- Move pointers forward and repeat.
- Handle final carry if present.

Time: O(max(m, n)) [length of linked list]
Space: O(max(m, n)) [length of result linked list]

'''
class SingleNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def add_numbers(num1, num2):
    dummy = SingleNode(0)
    temp = dummy
    carry = 0

    while (num1 is not None or num2 is not None) or carry:
        temp_sum = 0
        if num1 is not None:
            temp_sum += num1.data
            num1 = num1.next
        if num2 is not None:
            temp_sum += num2.data
            num2 = num2.next
        temp_sum += carry
        dig = temp_sum % 10
        carry = temp_sum // 10
        temp.next = SingleNode(dig)
        temp = temp.next
    
    return dummy.next
    

#num1  = 243, num2 = 564
a = SingleNode(2)
b = SingleNode(4)
c = SingleNode(3)

d = SingleNode(5)
e = SingleNode(6)
f = SingleNode(4)

a.next = b
b.next = c

d.next = e
e.next = f

h = add_numbers(a, d)
print_linked_list(h)
#Result: sum = 807; L = [7,0,8]

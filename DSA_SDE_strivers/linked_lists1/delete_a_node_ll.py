'''
Problem:
Write a function to delete a node in a singly-linked list.

Approach:
- Copy the value from node.next into node.
- Set node.next to node.next.next.
- The "next node" is removed from the list, and the "given node" now contains its value.

Time: O(1)
Space: O(1)


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

def delete_node(node):
    #input is the node to be deleted not the head
    node.data = node.next.data
    node.next = node.next.next



a = SingleNode(1)
b = SingleNode(3)
c = SingleNode(2)
d = SingleNode(4)

a.next = b
b.next = c
c.next = d

h = delete_node(c)
print_linked_list(a)
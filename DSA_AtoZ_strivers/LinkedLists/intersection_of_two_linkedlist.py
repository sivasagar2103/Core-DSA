class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


def find_intersection_bf(heada, headb):
    while headb is not None:
        temp = heada
        while temp is not None:
            if temp == headb:
                return headb.data
            temp = temp.next
        headb = headb.next
    return None

def find_intersection_lengths(heada, headb):
    #time: O(n+m)
    a1 = heada
    a2 = headb

    while a1 != a2:
        a1 = headb if a1 is None else a1.next
        a2 = heada if a2 is None else a2.next
    
    return a1.data

common = Node(11)
common.next = Node(5)
common.next.next = Node(6)

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)

a1.next = a2
a2.next = a3
a3.next = common

b1 = Node(11)
b2 = Node(12)

b1.next = b2
b2.next = common

res = find_intersection_lengths(a1, b1)
print(res)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert at head → O(1)
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        if self.tail is None:   # first node
            self.tail = new_node

        self.size += 1

    # Insert at tail → O(1)
    def insert_tail(self, value):
        new_node = Node(value)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node  # empty list

        self.tail = new_node
        self.size += 1

    # Insert at index → O(n)
    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.insert_head(value)
        if index == self.size:
            return self.insert_tail(value)

        new_node = Node(value)
        curr = self.head
        
        for _ in range(index - 1):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    # Delete head → O(1)
    def delete_head(self):
        if not self.head:
            return
        
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.size -= 1

    # Delete at index → O(n)
    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.delete_head()

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next

        if index == self.size - 1:  # deleting tail
            self.tail = curr

        self.size -= 1

    # Search → O(n)
    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    # Print list → O(n)
    def display(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        print(result)


ll = LinkedList()

ll.insert_head(10)
ll.insert_tail(20)
ll.insert_tail(30)
ll.insert_at(1, 15)
ll.print_list()

#10 -> 15 -> 20 -> 30 -> None

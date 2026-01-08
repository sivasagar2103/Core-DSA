class Stack:
    #using fixed array
    def __init__(self, limit):
        self.limit = limit #max size of stack
        self.stack_ds = [None] * limit #pre-allocate array memory
        self.top = -1 #top pointer
        
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.limit - 1
    
    def push(self, value):
        if self.is_full():
            print("stack over flow")
            return None
        self.top += 1
        self.stack_ds[self.top] = value
    
    def pop(self):
        if self.is_empty():
            print("stack underflow")
            return None
        pop_item = self.stack_ds[self.top]
        self.top -= 1
        return pop_item
    
    def peek(self):
        if self.is_empty():
            print("stack underflow")
            return None
        return self.stack_ds[self.top]
    
    def display(self):
        if self.is_empty():
            return None
        else:
            return self.stack_ds[: self.top + 1]

stack_obj = Stack(5)
stack_obj.push(49)
res = stack_obj.pop()
print(res)


class DynamicStack:
    #using list data type

    def __init__(self):
        self.stack_ds = []

    def is_empty(self):
        return len(self.stack_ds) == 0
    
    def push(self, value):
        self.stack_ds.append(value)
    
    def pop(self):
        if self.is_empty():
            print("stack under flow")
            return None
        return self.stack_ds.pop()
    
    def display(self):
        if self.is_empty():
            print("stack under flow")
            return None
        return self.stack_ds
    
    def peek(self):
        if self.is_empty():
            print("stack under flow")
            return None
        return self.stack_ds[-1]

d_stack = DynamicStack()
d_stack.push(20)
d_stack.push(30)
res = d_stack.display()
d_stack.pop()
print(res)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    #using linked list
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        popped_element = self.top.data
        self.top = self.top.next
        return popped_element
    
    def size(self):
        if self.is_empty():
            return None
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

l_stack = StackLinkedList()
l_stack.push(20)
l_stack.push(30)
popeed_ele = d_stack.pop()
print(popeed_ele)

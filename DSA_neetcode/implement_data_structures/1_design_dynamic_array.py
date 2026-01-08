
class DynamicArray:

    def __init__(self, capacity:int = 5):
        self._capacity = max(capacity, 1)
        self._data = [None] * self._capacity
        self._n = 0

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def is_empty(self):
        return self._n == 0
    
    def _resize(self, new_capacity : int):
        new_data = [None] * new_capacity
        for i in range(self._n):
            new_data.append(self._data[i])
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._n == self.capacity:
            self._resize(self.capacity * 2)
        self._data[self._n] = value
        self._n += 1
    
    def pop(self, index:int = -1):
        #index based removal of element
        if self._n == 0:
            raise IndexError("pop from empty array")
        if index < 0:
            index += self._n

        value = self._data[index]
        #removed index to last element
        #shift the elements to left
        for i in range(index, self._n-1):
            self._data[i] = self._data[i+1]
        self._data[self._n - 1] = None
        self._n -= 1
        #shrink if elements are very less
        return value
    
    def insert(self, value, index):

        if self._n == self.capacity:
            self._resize(self.capacity * 2)
        
        #move the elements from last to successive index
        #until the insertion position. shift towards right
        for i in range(self._n, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = value
        self._n += 1
    
    def remove(self, value):
        for i in range(self._n):
            if self._data[i] == value:
                self.pop(i)
                return
    
    def clear(self):
        self._data = [None] * 1
        self._n = 0
        self._capacity = 1
    
    def extend(self, values):
        for v in values:
            self.append(v)


a = DynamicArray()

for i in range(10):
    a.append(i)

print(a.pop())

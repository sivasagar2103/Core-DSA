class SingleNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None


class DoubleNode:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = None
        self.next = None

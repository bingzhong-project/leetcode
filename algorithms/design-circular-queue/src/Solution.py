class MyCircularQueue:
    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k + 1
        self.table = [None for _ in range(self.size)]
        self.head = 0
        self.tail = 0

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.table[self.tail] = value
            self.tail = 0 if self.tail + 1 == self.size else self.tail + 1
            return True

    def deQueue(self) -> 'bool':
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.head = 0 if self.head + 1 == self.size else self.head + 1
            return True

    def Front(self) -> 'int':
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.table[self.head]

    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            pos = self.tail - 1
            return self.table[pos] if pos > -1 else self.table[self.size + pos]

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> 'bool':
        """
        Checks whether the circular queue is full or not.
        """
        return self.head == ((self.tail + 1) % self.size)

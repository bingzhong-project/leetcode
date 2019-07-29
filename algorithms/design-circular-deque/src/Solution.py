class MyCircularDeque:
    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k + 1
        self.table = [None for _ in range(k + 1)]
        self.head = 0
        self.tail = self.head

    def insertFront(self, value: 'int') -> 'bool':
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.head = (self.head - 1 + self.size * 2) % self.size
            self.table[self.head] = value
            return True

    def insertLast(self, value: 'int') -> 'bool':
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.table[self.tail] = value
            self.tail = (self.tail + 1) % self.size
            return True

    def deleteFront(self) -> 'bool':
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.size
            return True

    def deleteLast(self) -> 'bool':
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail - 1 + self.size * 2) % self.size
            return True

    def getFront(self) -> 'int':
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.table[self.head]

    def getRear(self) -> 'int':
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.table[
            (self.tail - 1 + self.size * 2) % self.size]

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> 'bool':
        """
        Checks whether the circular deque is full or not.
        """
        return self.head == (self.tail + 1) % self.size

class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [False for _ in range(1000000)]

    def add(self, key: int) -> None:
        self.table[key] = True

    def remove(self, key: int) -> None:
        self.table[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.table[key]

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None for _ in range(10000)]
        self.size = 10000

    def add(self, key: int) -> None:
        index = key % self.size
        node = self.table[index]
        if node:
            while node:
                if node.val == key:
                    return
                node = node.next
            cur = self.table[index]
            prepare = ListNode(key)
            self.table[index] = prepare
            prepare.next = cur
        else:
            self.table[index] = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        dummy = ListNode(None)
        dummy.next = self.table[index]
        node = self.table[index]
        pre = dummy
        while node:
            if node.val == key:
                pre.next = node.next
                node.next = None
                break
            pre = node
            node = node.next
        self.table[index] = dummy.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        node = self.table[index]
        while node:
            if node.val == key:
                return True
            node = node.next

        return False

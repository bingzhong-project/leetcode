class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Entry:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None for _ in range(10000)]
        self.size = 10000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        node = self.table[index]
        if node:
            while node:
                if node.val.key == key:
                    node.val.val = value
                    return
                node = node.next
            cur = self.table[index]
            prepare = ListNode(Entry(key, value))
            self.table[index] = prepare
            prepare.next = cur
        else:
            self.table[index] = ListNode(Entry(key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        node = self.table[index]
        while node:
            if node.val.key == key:
                return node.val.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        dummy = ListNode(None)
        dummy.next = self.table[index]
        node = self.table[index]
        pre = dummy
        while node:
            if node.val.key == key:
                pre.next = node.next
                node.next = None
                break
            pre = node
            node = node.next
        self.table[index] = dummy.next

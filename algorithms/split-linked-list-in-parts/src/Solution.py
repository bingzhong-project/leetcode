# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> list:
        size = 0
        node = root
        while node:
            size += 1
            node = node.next
        div, mod = divmod(size, k)
        split_sizes = [0 for _ in range(k)]
        for i in range(len(split_sizes)):
            split_size = div
            if mod > 0:
                split_size += 1
                mod -= 1
            split_sizes[i] = split_size

        res = [None for _ in range(k)]
        node = root
        for i in range(len(split_sizes)):
            res[i] = node
            split_size = split_sizes[i]
            while split_size > 1 and node:
                node = node.next
                split_size -= 1
            if node:
                next_node = node.next
                node.next = None
                node = next_node

        return res

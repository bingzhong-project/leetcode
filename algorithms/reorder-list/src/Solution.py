# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        cache = []
        node = head
        while node is not None:
            cache.append(node)
            node = node.next
        node = head
        for i in range(len(cache) - 1, len(cache) // 2, -1):
            next_node = node.next
            node.next = cache[i]
            cache[i].next = next_node
            cache[i - 1].next = None
            node = next_node

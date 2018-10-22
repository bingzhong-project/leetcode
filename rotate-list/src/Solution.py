# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        length = 0
        node = head
        tail = None
        while node is not None:
            length += 1
            tail = node
            node = node.next
        n = length - k % length
        if n == 0 or n == length:
            return dummy.next
        last_node = dummy
        for i in range(n):
            last_node = last_node.next
        next_node = last_node.next
        tail.next = head
        dummy.next = next_node
        last_node.next = None

        return dummy.next

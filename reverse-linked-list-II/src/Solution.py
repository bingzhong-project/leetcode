# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        i = 0
        node = dummy
        start = None
        end = None
        while node is not None:
            if i == m - 1:
                start = node
            if i == n + 1:
                end = node
                break
            i += 1
            node = node.next
        point = start.next
        while point.next != end:
            next_node = point.next
            point.next = next_node.next
            next_node.next = start.next
            start.next = next_node
        return dummy.next

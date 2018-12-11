# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = head
        while node is not None and node.next is not None:
            val = node.next.val
            if node.val < val:
                node = node.next
                continue
            if prev.next.val > val:
                prev = dummy
            while prev.next.val < val:
                prev = prev.next
            next_node = node.next
            node.next, next_node.next, prev.next = next_node.next, prev.next, next_node
        return dummy.next

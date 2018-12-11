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
        cur = head
        while cur is not None and cur.next is not None:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if prev.next.val > val:
                prev = dummy
            while prev.next.val < val:
                prev = prev.next
            next_node = cur.next
            cur.next, next_node.next, prev.next = next_node.next, prev.next, next_node
        return dummy.next

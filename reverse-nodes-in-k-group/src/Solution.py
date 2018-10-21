# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def reverse(start, end):
            cur = start.next
            while cur.next != end:
                next_node = cur.next
                cur.next = next_node.next
                next_node.next = start.next
                start.next = next_node
            return [start.next, cur]

        i = 1
        new_head = None
        start = ListNode(-1)
        start.next = head
        end = head
        while end is not None:
            end = end.next
            if i % k == 0:
                result = reverse(start, end)
                start = result[1]
                if new_head is None:
                    new_head = result[0]
            i += 1
        if new_head is None:
            new_head = head
        return new_head

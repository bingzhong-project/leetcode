# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        end = None
        while start is not None:
            node = start.next
            times = 0
            while node is not None:
                end = node.next
                if end is None:
                    break
                if node.val != end.val:
                    break
                node = node.next
                times += 1
            if times == 0:
                start = start.next
            else:
                start.next = end
        return dummy.next

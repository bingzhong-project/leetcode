# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        node = head
        while node.next is not None:
            next_node = node.next
            node.next = next_node.next
            next_node.next = dummy.next
            dummy.next = next_node
        return dummy.next

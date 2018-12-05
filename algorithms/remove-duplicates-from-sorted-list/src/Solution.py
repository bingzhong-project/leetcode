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
        node = head
        pre_node = ListNode(-1)
        while node is not None:
            if node.val == pre_node.val:
                pre_node.next = node.next
                node = pre_node
            else:
                pre_node = node
            node = node.next

        return head

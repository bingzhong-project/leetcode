# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        node = head
        previous_node = node
        while node is not None:
            next_node = node.next
            if next_node is None:
                break
            after_node = next_node.next
            node.next = after_node
            next_node.next = node
            if previous_node == head:
                head = next_node
            else:
                previous_node.next = next_node
            previous_node = node
            node = after_node

        return head

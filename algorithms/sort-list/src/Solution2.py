# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        快速排序

        :type head: ListNode
        :rtype: ListNode
        """

        def middle(node, tail):
            slow = node
            fast = node
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        def swap(node1, prev_node1, node2, prev_node2):
            prev_node1.next, prev_node2.next = node2, node1
            node1.next, node2.next = node2.next, node1.next

        def sort(head, tail):
            if head == tail:
                return
            pass

        sort(head, None)
        return head

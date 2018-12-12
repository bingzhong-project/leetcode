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

        def middle(node):
            slow = node
            fast = node
            prev = slow
            while fast is not None and fast.next is not None:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev

        def sort(head, tail):
            if head.next is None:
                return
            dummy = ListNode(None)
            dummy.next = head
            prev_middle_node = middle(head)
            middle_node = prev_middle_node.next

            i = dummy.next
            while i != middle_node:
                if i.val > middle_node.val:
                    middle_node_next = middle_node.next
                    i_next = i.next
                    middle_node.next, i.next, i = i, middle_node_next, i_next

            j = middle_node.next
            while j.next != tail:
                if j.val < middle_node.val:
                    dummy_next = dummy.next
                    j_next = j.next
                    dummy.next, j.next, j = j, dummy_next, j_next
            sort(head, middle_node)
            sort(middle_node.next, None)
        sort(head)
        return head

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
            if head is None or head.next is None:
                return
            dummy = ListNode(None)
            dummy.next = head
            middle_node = middle(head)

            i = dummy.next
            while i != middle_node:
                i_next = i.next
                if i.val > middle_node.val:
                    middle_node_next = middle_node.next
                    i_next = i.next
                    middle_node.next, i.next = i, middle_node_next
                i = i_next

            j = middle_node.next
            while j is not None and j.next != tail:
                j_next = j.next
                if j.val < middle_node.val:
                    dummy_next = dummy.next
                    j_next = j.next
                    dummy.next, j.next = j, dummy_next
                j = j_next
            sort(dummy.next, middle_node)
            sort(middle_node.next, None)

        sort(head, None)
        return head


# if __name__ == '__main__':
#     node1 = ListNode(1)
#     node2 = ListNode(2)
#     node3 = ListNode(3)
#     node4 = ListNode(4)
#     node4.next = node2
#     node2.next = node1
#     node1.next = node3
#     Solution().sortList(node4)

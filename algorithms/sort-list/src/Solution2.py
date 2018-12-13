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

        def swap_val(node1, node2):
            tmp = node1.val
            node1.val = node2.val
            node2.val = tmp

        def sort(head, tail):
            if head == tail or head.next is None:
                return
            val = head.val
            swap = head
            current = swap.next
            while current != tail:
                if current.val < val:
                    swap = swap.next
                    if swap != current:
                        swap_val(current, swap)
                current = current.next
            if head != current:
                swap_val(head, swap)
            sort(head, swap)
            sort(swap.next, tail)

        sort(head, None)
        return head

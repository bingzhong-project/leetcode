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
        insert = dummy
        sort_tail = head
        while sort_tail is not None and sort_tail.next is not None:
            val = sort_tail.next.val
            if sort_tail.val < val:
                sort_tail = sort_tail.next
                continue
            if insert.next.val > val:
                insert = dummy
            while insert.next.val < val:
                insert = insert.next
            next_node = sort_tail.next
            sort_tail.next, next_node.next, insert.next = next_node.next, insert.next, next_node
        return dummy.next

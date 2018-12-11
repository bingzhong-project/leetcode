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
        node = head
        pre = dummy
        while node is not None:
            insert_point = dummy
            next_node = node.next
            while True:
                if insert_point.next == node:
                    pre = node
                    break
                if insert_point.next.val > node.val:
                    next_insert_point = insert_point.next
                    insert_point.next = node
                    node.next = next_insert_point
                    pre.next = next_node
                    break
                insert_point = insert_point.next
            node = next_node
        return dummy.next

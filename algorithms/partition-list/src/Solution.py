# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        front = dummy
        back = front.next
        while back is not None:
            if back.val < x:
                front = front.next
                back = back.next
            else:
                break
        insert = front
        while back is not None:
            if back.val >= x:
                front = front.next
                back = back.next
            else:
                front.next = back.next
                insert_next = insert.next
                insert.next = back
                back.next = insert_next
                back = front.next
                insert = insert.next
        return dummy.next

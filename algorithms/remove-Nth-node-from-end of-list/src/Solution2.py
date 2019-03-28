# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        dummy = ListNode(None)
        dummy.next = head
        front, back = dummy, dummy
        for i in range(n):
            back = back.next
        while back.next:
            front = front.next
            back = back.next

        front.next = front.next.next

        return dummy.next

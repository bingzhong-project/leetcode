# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        sentinel = ListNode(-1)
        tail = sentinel
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        while l1:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        while l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        return sentinel.next

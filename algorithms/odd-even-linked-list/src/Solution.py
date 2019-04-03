# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return head
        odd = head
        even = head.next
        while even and even.next:
            odd_next = odd.next
            odd.next = even.next
            even.next = even.next.next
            odd.next.next = odd_next
            odd = odd.next
            even = even.next
        return head

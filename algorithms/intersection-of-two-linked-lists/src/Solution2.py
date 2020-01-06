# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        tailA = headA
        while tailA.next:
            tailA = tailA.next
        tailA.next = headA
        slow = headB
        fast = headB
        while fast and fast.next:
            pass

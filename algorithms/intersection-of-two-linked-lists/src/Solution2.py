# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        tailA = headA
        while tailA.next:
            tailA = tailA.next
        tailA.next = headA
        slow = headB
        fast = headB
        circle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                circle = True
                break
        if not circle:
            tailA.next = None
            return None
        start = headB
        while start and slow:
            if start == slow:
                tailA.next = None
                return start
            start = start.next
            slow = slow.next

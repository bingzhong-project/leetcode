# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        a_size = 0
        b_size = 0

        node = headA
        while node:
            a_size += 1
            node = node.next

        node = headB
        while node:
            b_size += 1
            node = node.next

        if a_size > b_size:
            l_node = headA
            s_node = headB
        else:
            l_node = headB
            s_node = headA
        diff = abs(a_size - b_size)
        for i in range(diff):
            l_node = l_node.next
        while l_node and s_node:
            if l_node == s_node:
                return l_node
            l_node = l_node.next
            s_node = s_node.next

        return None

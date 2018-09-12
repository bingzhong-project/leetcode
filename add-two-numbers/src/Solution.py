# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_node = None
        node1 = l1
        node2 = l2
        is_carry = False
        previous_node = None
        while node1 is not None or node2 is not None:
            if node1 is not None:
                val1 = node1.val
            else:
                val1 = 0
            if node2 is not None:
                val2 = node2.val
            else:
                val2 = 0
            sum = val1 + val2
            if is_carry:
                sum = sum + 1
            if sum >= 10:
                val = int(sum % 10)
                is_carry = True
            else:
                val = sum
                is_carry = False
            node = ListNode(val)
            if res_node is None:
                res_node = node
                previous_node = res_node
            else:
                previous_node.next = node
                previous_node = node
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        if is_carry:
            previous_node.next = ListNode(1)
        return res_node

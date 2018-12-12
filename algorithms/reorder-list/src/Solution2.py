# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        def middle(node):
            slow = node
            fast = node
            prev = slow
            while fast is not None and fast.next is not None:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev

        def reverse(node):
            dummy = ListNode(-1)
            dummy.next = node
            while node.next is not None:
                next_node = node.next
                node.next = next_node.next
                next_node.next = dummy.next
                dummy.next = next_node
            return dummy.next

        def merge(node1, node2):
            while node1 is not None:
                next_node1 = node1.next
                next_node2 = node2.next
                node1.next = node2
                if next_node1 is not None:
                    node2.next = next_node1
                node1 = next_node1
                node2 = next_node2

        if head is not None and head.next is not None:
            middle_node = middle(head)
            second_head = middle_node.next
            middle_node.next = None
            second_head = reverse(second_head)
            merge(head, second_head)

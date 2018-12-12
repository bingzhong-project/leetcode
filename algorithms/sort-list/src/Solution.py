# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
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

        def separate(head):
            middle_prev_node = middle(head)
            middle_node = middle_prev_node.next
            middle_prev_node.next = None
            return head, middle_node

        def merge(head1, head2):
            dummy = ListNode(None)
            tail = dummy
            node1 = head1
            node2 = head2
            while node1 is not None and node2 is not None:
                if node1.val < node2.val:
                    tail.next, node1 = node1, node1.next
                else:
                    tail.next, node2 = node2, node2.next
                tail = tail.next
            if node1 is not None:
                tail.next = node1
            elif node2 is not None:
                tail.next = node2
            return dummy.next

        def sort(head):
            if head.next is None:
                return head
            head1, head2 = separate(head)
            head1 = sort(head1)
            head2 = sort(head2)
            return merge(head1, head2)

        return sort(head) if head is not None else None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        快速排序

        :type head: ListNode
        :rtype: ListNode
        """

        def swap(node1, node2):
            tmp = node1.val
            node1.val = node2.val
            node2.val = tmp

        def sort(head, tail):
            if head == tail or head.next is None:
                return
            val = head.val
            switch = head
            i = head.next
            while i != tail:
                if i.val < val:
                    switch = switch.next
                    if switch != i:
                        swap(i, switch)

        sort(head, None)
        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node4.next = node2
    node2.next = node1
    node1.next = node3
    Solution().sortList(node4)

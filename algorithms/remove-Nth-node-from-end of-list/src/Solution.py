class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        array_list = list()
        node = head
        while node is not None:
            array_list.append(node)
            node = node.next
        remove_node = array_list[-n]
        if n == len(array_list):
            head = remove_node.next
        else:
            remove_node = array_list[-n]
            prev_node = array_list[-n - 1]
            prev_node.next = remove_node.next

        return head

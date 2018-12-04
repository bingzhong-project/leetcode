# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def build(node):
            if node is None:
                return None
            if node.next is None:
                return TreeNode(node.val)
            fast = node
            slow = node
            pre = slow
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                pre = slow
                slow = slow.next
            pre.next = None
            root = TreeNode(slow.val)
            root.left = build(node)
            root.right = build(slow.next)

            return root

        return build(head)


# class Solution:
#     def sortedListToBST(self, head):
#         """
#         :type head: ListNode
#         :rtype: TreeNode
#         """

#         def convert(list_node, left, right):
#             if left > right:
#                 return None
#             middle = int((left + right) / 2)
#             left_node = convert(list_node, left, middle - 1)
#             root = TreeNode(list_node[0].val)
#             root.left = left_node
#             list_node[0] = list_node[0].next
#             right_node = convert(list_node, middle + 1, right)
#             root.right = right_node

#             return root

#         length = 0
#         node = head
#         while node is not None:
#             node = node.next
#             length += 1
#         return convert([head], 0, length - 1)

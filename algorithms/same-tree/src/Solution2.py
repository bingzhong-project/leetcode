# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def is_same(p_node, q_node):
            if p_node is None or q_node is None:
                return p_node == q_node
            if p_node.val != q_node.val:
                return False
            else:
                return is_same(p_node.left, q_node.left) and is_same(
                    p_node.right, q_node.right)

        return is_same(p, q)

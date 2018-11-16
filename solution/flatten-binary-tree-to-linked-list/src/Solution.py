# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if node is None:
                return
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
            tmp_node = node.right
            node.right = node.left
            node.left = None
            while node.right is not None:
                node = node.right
            node.right = tmp_node

        return dfs(root)

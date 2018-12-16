# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, level, res):
            if node.left is None and node.right is None:
                res[0] = max(level, res[0])
            if node.left is not None:
                dfs(node.left, level + 1, res)
            if node.right is not None:
                dfs(node.right, level + 1, res)

        if root is None:
            return 0
        res = [1]
        dfs(root, 1, res)
        return res[0]

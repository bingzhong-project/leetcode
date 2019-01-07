# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, level, max_level, res):
            if node.left is None and node.right is None:
                if level > max_level[0]:
                    res[0] = node.val
                    max_level[0] = level
            if node.left is not None:
                dfs(node.left, level + 1, max_level, res)
            if node.right is not None:
                dfs(node.right, level + 1, max_level, res)

        if root is None:
            return 0
        res = [0]
        dfs(root, 0, [-1], res)

        return res[0]

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

        def dfs(node):
            if node is None:
                return 0
            left_level = dfs(node.left) + 1
            right_level = dfs(node.right) + 1
            return max(left_level, right_level)

        return dfs(root)

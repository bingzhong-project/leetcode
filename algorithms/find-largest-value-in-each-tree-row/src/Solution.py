# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        MIN_VALUE = -2**31

        def dfs(node, level, res):
            if level not in res:
                res[level] = MIN_VALUE
            res[level] = max(res[level], node.val)
            if node.left is not None:
                dfs(node.left, level + 1, res)
            if node.right is not None:
                dfs(node.right, level + 1, res)

        if root is None:
            return []
        res = dict()
        dfs(root, 0, res)

        return list(res.values())

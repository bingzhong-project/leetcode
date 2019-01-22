# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def dfs(node, depth, res):
            if depth not in res:
                res[depth] = node.val
            if node.right is not None:
                dfs(node.right, depth + 1, res)
            if node.left is not None:
                dfs(node.left, depth + 1, res)

        if root is None:
            return []
        res = {}
        dfs(root, 0, res)
        return list(res.values())

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node, min_val, max_val):
            if node is None:
                return True
            if (min_val is not None
                    and node.val <= min_val) or (max_val is not None
                                                 and node.val >= max_val):
                return False
            return dfs(node.left, min_val, node.val) and dfs(
                node.right, node.val, max_val)

        return dfs(root, None, None)

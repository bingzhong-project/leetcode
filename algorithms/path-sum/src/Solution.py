# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs(node, target):
            if node.left is None and node.right is None:
                return target - node.val == 0
            left_result = False if node.left is None else dfs(
                node.left, target - node.val)
            right_result = False if node.right is None else dfs(
                node.right, target - node.val)
            return left_result or right_result

        if root is None:
            return False
        return dfs(root, sum)

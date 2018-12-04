# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if node is None:
                return [0, 0]
            left_money = dfs(node.left)
            right_money = dfs(node.right)
            node_money = [0, 0]
            node_money[0] = max(left_money[0], left_money[1]) + max(
                right_money[0], right_money[1])
            node_money[1] = node.val + left_money[0] + right_money[0]
            return node_money

        money = dfs(root)
        return max(money)

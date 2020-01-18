# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, high, max_high, res):
            if node is None:
                return high

            left_high = dfs(node.left, high + 1, max_high, res)
            right_high = dfs(node.right, high + 1, max_high, res)
            if left_high == right_high and left_high >= max_high[0]:
                res[0] = node
                max_high[0] = max(left_high, right_high)

            return max(left_high, right_high)

        res = [None]
        dfs(root, 0, [0], res)

        return res[0]

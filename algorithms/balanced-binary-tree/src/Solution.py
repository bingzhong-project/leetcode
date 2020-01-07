# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True

        def dfs(node):
            if node is None:
                return 0
            left_height = dfs(node.left) + 1
            right_height = dfs(node.right) + 1

            if abs(left_height - right_height) > 1:
                self.res = False

            return max(left_height, right_height)

        dfs(root)

        return self.res

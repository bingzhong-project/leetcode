# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        self.res = 0

        def dfs(node):
            if node.left:
                if node.left.left is None and node.left.right is None:
                    self.res += node.left.val
                dfs(node.left)
            if node.right:
                dfs(node.right)

        if root:
            dfs(root)
        return self.res

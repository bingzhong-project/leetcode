# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        def dfs(t1, t2):
            if t1 is None and t2 is None:
                return None
            val1 = 0 if t1 is None else t1.val
            val2 = 0 if t2 is None else t2.val
            node = TreeNode(val1 + val2)
            node.left = dfs(t1.left if t1 else None, t2.left if t2 else None)
            node.right = dfs(t1.right if t1 else None, t2.right if t2 else None)
            return node

        return dfs(t1, t2)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        def dfs(node, visited, k, res):
            if node is None:
                return
            if res[0]:
                return
            dfs(node.left, visited, k, res)
            visited.add(k - node.val)
            dfs(node.right, visited, k, res)
            if node.val != k - node.val and node.val in visited:
                res[0] = True
                return

        res = [False]
        dfs(root, set(), k, res)

        return res[0]

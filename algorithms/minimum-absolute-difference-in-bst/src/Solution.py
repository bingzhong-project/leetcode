# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: 'TreeNode') -> 'int':
        def dfs(root, nodes):
            if root.left:
                dfs(root.left, nodes)
            nodes.append(root.val)
            if root.right:
                dfs(root.right, nodes)

        nodes = []
        dfs(root, nodes)
        res = 2**31
        for i in range(1, len(nodes)):
            res = min(res, nodes[i] - nodes[i - 1])
        return res

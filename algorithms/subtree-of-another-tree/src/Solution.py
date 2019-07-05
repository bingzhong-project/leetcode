# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        def dfs(node, array):
            if node:
                array.append(node.val)
                if node.left:
                    dfs(node.left, array)
                if node.right:
                    dfs(node.right, array)

        def func(node, array, res):
            if node is None:
                return []
            left_path = func(node.left, array, res)
            right_path = func(node.right, array, res)
            node_path = [node.val] + left_path + right_path
            if node_path == array:
                res[0] = True
            return node_path

        array = []
        dfs(t, array)

        res = [False]
        func(s, array, res)

        return res[0]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        def search(root, target):
            if root is None:
                return False
            if root.val > target:
                return search(root.left, target)
            elif root.val < target:
                return search(root.right, target)
            else:
                return True

        def dfs(root, node, k, res):
            if root is None:
                return
            if node is None:
                return
            target = k - node.val
            if target != node.val:
                if search(root, target):
                    res[0] = True
                    return
                if search(root, target):
                    res[0] = True
                    return
            dfs(root, node.left, k, res)
            dfs(root, node.right, k, res)

        res = [False]
        dfs(root, root, k, res)

        return res[0]

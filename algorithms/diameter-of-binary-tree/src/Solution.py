# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        def max_height(node, cache):
            if node in cache:
                return cache[node]
            res = 0
            if node:
                left_height = max_height(node.left, cache) + 1
                right_height = max_height(node.right, cache) + 1
                res = max(left_height, right_height)
            cache[node] = res
            return res

        if root is None:
            return 0
        cache = {}
        res = 0
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            left_max_height = max_height(node.left, cache)
            right_max_height = max_height(node.right, cache)
            res = max(res, left_max_height + right_max_height)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        stack = []
        node = root
        last = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or last == node.right:
                stack.pop()
                res.append(node.val)
                last = node
                node = None
                continue
            node = node.right

        return res

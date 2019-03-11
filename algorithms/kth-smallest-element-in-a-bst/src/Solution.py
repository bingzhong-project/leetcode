# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: 'TreeNode', k: 'int') -> 'int':
        stack = []
        count = 0
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
            node = node.right
        return -1

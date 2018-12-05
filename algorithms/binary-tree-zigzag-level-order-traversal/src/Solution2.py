# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        stack1 = []
        stack2 = []
        cache = []
        if root is not None:
            stack1.append(root)
        while len(stack1) > 0 or len(stack2) > 0:
            while len(stack1) > 0:
                node = stack1.pop()
                cache.append(node.val)
                if node.left is not None:
                    stack2.append(node.left)
                if node.right is not None:
                    stack2.append(node.right)
            if len(cache) > 0:
                res.append(cache)
                cache = []
            while len(stack2) > 0:
                node = stack2.pop()
                cache.append(node.val)
                if node.right is not None:
                    stack1.append(node.right)
                if node.left is not None:
                    stack1.append(node.left)
            if len(cache) > 0:
                res.append(cache)
                cache = []
        return res

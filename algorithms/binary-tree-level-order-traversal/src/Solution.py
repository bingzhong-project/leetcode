# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = list()
        last = root
        cache = []
        if root is not None:
            queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            cache.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node == last:
                if len(queue) > 0:
                    last = queue[-1]
                res.append(cache)
                cache = []
        return res

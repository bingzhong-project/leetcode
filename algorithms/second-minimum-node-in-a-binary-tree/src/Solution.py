# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> 'int':
        if root is None:
            return -1

        queue = []
        queue.append(root)
        min_val = root.val
        res = 2**31
        while queue:
            level_min = 2**31
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left and node.right:
                    if node.left.val != min_val and level_min > node.left.val:
                        level_min = node.left.val
                    if node.right.val != min_val and level_min > node.right.val:
                        level_min = node.right.val
                    queue.append(node.left)
                    queue.append(node.right)
            if level_min != 2**31:
                res = min(res, level_min)
        return res if res != 2**31 else -1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        res = []

        queue = []
        if root:
            queue.append(root)
        while queue:
            count = len(queue)
            sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum / count)
        return res

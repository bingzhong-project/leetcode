# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0

        queue = []
        queue.append((root, 0))
        res = 1
        while queue:
            start = None
            end = None
            for _ in range(len(queue)):
                node, index = queue.pop(0)
                if node.left:
                    left_index = 2 * index
                    start = left_index if start is None else start
                    end = left_index
                    queue.append((node.left, left_index))
                if node.right:
                    right_index = 2 * index + 1
                    start = right_index if start is None else start
                    end = right_index
                    queue.append((node.right, right_index))
            width = 0
            if start is not None and end is not None:
                width = end - start + 1
            res = max(res, width)
        return res

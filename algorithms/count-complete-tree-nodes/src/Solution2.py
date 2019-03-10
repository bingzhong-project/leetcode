# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: 'TreeNode') -> 'int':
        def depth(node):
            if node is None:
                return 0
            return depth(node.left) + 1

        def count(node):
            if node is None:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            if left_depth == right_depth:
                return 2**left_depth + count(node.right)
            else:
                return 2**right_depth + count(node.left)

        return count(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        self.ans = 0
        self.height(root)
        return self.ans

    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        self.ans = max(self.ans, left_height + right_height)
        return max(left_height, right_height) + 1

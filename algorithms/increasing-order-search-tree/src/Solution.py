# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.p = TreeNode(None)

        def func(node):
            if node.left:
                func(node.left)
            node.left = None
            self.p.right = node
            self.p = self.p.right
            if node.right:
                func(node.right)

        sentinel = TreeNode(None)
        sentinel.right = self.p
        func(root)

        return sentinel.right

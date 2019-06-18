# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        def convert(node, val):
            if node.right:
                convert(node.right, val)
            node.val += val[0]
            val[0] = node.val
            if node.left:
                convert(node.left, val)

        if root:
            convert(root, [0])

        return root

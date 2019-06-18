# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        def traverse(node, vals):
            if node.left:
                traverse(node.left, vals)
            vals.append(node.val)
            if node.right:
                traverse(node.right, vals)

        def convert(node, vals):
            if node.left:
                convert(node.left, vals)
            node.val = sum(vals)
            vals.pop(0)
            if node.right:
                convert(node.right, vals)

        if root is None:
            return root

        vals = []
        traverse(root, vals)
        convert(root, vals)

        return root

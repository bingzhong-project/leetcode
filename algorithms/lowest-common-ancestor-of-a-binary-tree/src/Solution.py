# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q, res):
            if node.left:
                lca(node.left, p, q, res)
            if node.right:
                lca(node.right, p, q, res)
            if (node.left and node.left.val == p.val) or (
                    node.right and node.right.val == p.val):
                p.val = node.val
            if (node.left and node.left.val == q.val) or (
                    node.right and node.right.val == q.val):
                q.val = node.val
            if p.val == q.val and res.val is None:
                res.val = p.val

        res = TreeNode(None)
        if root:
            lca(root, p, q, res)
        return res

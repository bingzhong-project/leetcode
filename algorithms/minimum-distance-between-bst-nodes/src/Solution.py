# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def func(node, pre, res):
            if node.left:
                func(node.left, pre, res)
            if pre[0]:
                res[0] = min(node.val - pre[0].val, res[0])
            pre[0] = node
            if node.right:
                func(node.right, pre, res)

        if root is None:
            return 0

        res = [root.val]
        func(root, [None], res)
        return res[0]

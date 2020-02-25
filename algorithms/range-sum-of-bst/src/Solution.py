# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0

        def func(node, l, r):
            if node.val >= l and node.val <= r:
                self.res += node.val
                func(node.left, l, r)
                func(node.right, l, r)
            elif node.val < l:
                func(node.right, l, r)
            elif node.val > r:
                func(node.left, l, r)

        func(root, L, R)

        return self.res

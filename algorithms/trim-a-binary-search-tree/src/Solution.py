# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'TreeNode':
        def trim(root, L, R):
            if root is None:
                return None
            root.left = trim(root.left, L, R)
            root.right = trim(root.right, L, R)
            if root.val < L:
                return root.right
            if root.val > R:
                return root.left
            return root

        if root is None:
            return root

        dummy = TreeNode(L)
        dummy.left = root
        trim(dummy, L, R)

        return dummy.left

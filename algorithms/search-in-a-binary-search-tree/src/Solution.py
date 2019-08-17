# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(root, val):
            if root is None:
                return None
            if root.val > val:
                return search(root.left, val)
            elif root.val < val:
                return search(root.right, val)
            else:
                return root

        return search(root, val)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: 'TreeNode', key: 'int') -> 'TreeNode':
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                root.val = self.findMin(root.right).val
                root.right = self.deleteNode(root.right, root.val)
            else:
                root = root.left if root.left else root.right

        return root

    def findMin(self, root):
        return self.findMin(root.left) if root.left else root

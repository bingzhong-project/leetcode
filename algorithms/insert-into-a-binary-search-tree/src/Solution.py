# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(node, val):
            if node.val > val:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)

        if root is None:
            return TreeNode(val)

        insert(root, val)

        return root

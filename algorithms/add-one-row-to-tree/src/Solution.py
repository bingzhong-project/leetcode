# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: 'TreeNode', v: 'int', d: 'int') -> 'TreeNode':
        def dfs(node, v, d, depth=1):
            left_child = node.left
            right_child = node.right
            if depth == d - 1:
                left_new_child = TreeNode(v)
                right_new_child = TreeNode(v)
                left_new_child.left = left_child
                right_new_child.right = right_child
                node.left = left_new_child
                node.right = right_new_child
            if left_child:
                dfs(left_child, v, d, depth + 1)
            if right_child:
                dfs(right_child, v, d, depth + 1)

        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            dfs(root, v, d)
            return root

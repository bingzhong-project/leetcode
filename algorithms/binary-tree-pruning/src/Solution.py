# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(node):
            if node.left is None and node.right is None:
                return node.val
            node_sum = 0
            if node.left:
                left_sum = node.left.val + prune(node.left)
                if left_sum == 0:
                    node.left = None
                node_sum += left_sum
            if node.right:
                right_sum = node.right.val + prune(node.right)
                if right_sum == 0:
                    node.right = None
                node_sum += right_sum

            return node_sum + node.val

        prune(root)

        return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node, leaves):
            if node.left is None and node.right is None:
                leaves.append(node.val)
            if node.left:
                dfs(node.left, leaves)
            if node.right:
                dfs(node.right, leaves)

        leaves_1 = []
        leaves_2 = []
        dfs(root1, leaves_1)
        dfs(root2, leaves_2)

        if len(leaves_1) != len(leaves_2):
            return False
        for x, y in list(zip(leaves_1, leaves_2)):
            if x != y:
                return False

        return True

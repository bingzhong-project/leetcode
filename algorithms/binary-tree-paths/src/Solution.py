# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def dfs(node, path, paths):
            node_val = str(node.val)
            if node.left is None and node.right is None:
                path += [node_val]
                paths.append('->'.join(path))
            if node.left is not None:
                dfs(node.left, path + [node_val], paths)
            if node.right is not None:
                dfs(node.right, path + [node_val], paths)

        if root is None:
            return []
        paths = []
        dfs(root, [], paths)

        return paths

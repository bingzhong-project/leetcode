# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        def dfs(node):
            if node is None:
                return 0
            max_depth = 1
            for child in node.children:
                max_depth = max(max_depth, dfs(child) + 1)

            return max_depth

        return dfs(root) if root else 0

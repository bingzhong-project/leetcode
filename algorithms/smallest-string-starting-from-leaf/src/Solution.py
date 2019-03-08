# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        def dfs(node):
            if node is None:
                return None
            else:
                char = chr(node.val + ord('a'))
                ls = dfs(node.left)
                rs = dfs(node.right)
                if ls is None and rs is None:
                    return char
                elif ls and rs is None:
                    return ls + char
                elif ls is None and rs:
                    return rs + char
                else:
                    return min(ls, rs) + char

        return dfs(root)

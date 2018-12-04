# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def dfs(node, elements):
            if node is not None:
                elements.append(node.val)
            else:
                elements.append(None)
                return
            dfs(node.left, elements)
            dfs(node.right, elements)

        p_elements = []
        q_elements = []
        dfs(p, p_elements)
        dfs(q, q_elements)
        return p_elements == q_elements

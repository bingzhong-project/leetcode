# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        stack = []
        visited = []
        stack.append(root)
        visited.append(root)
        while len(stack) > 0:
            node = stack[-1]
            if (node.left is None
                    or node.left in visited) and (node.right is None
                                                  or node.right in visited):
                res.append(stack.pop().val)
                continue
            if node.left is not None and node.left not in visited:
                stack.append(node.left)
                visited.append(node.left)
            else:
                res.append(stack.pop().val)
                if node.right is not None and node.right not in visited:
                    stack.append(node.right)
                    visited.append(node.right)

        return res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        node = root
        pre_node = None
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            node = stack[-1]
            if (node.left is None and node.right is None) or (
                    pre_node is not None and (pre_node == node.left or pre_node == node.right)):
                res.append(stack.pop().val)
                pre_node = node
            else:
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)

        return res

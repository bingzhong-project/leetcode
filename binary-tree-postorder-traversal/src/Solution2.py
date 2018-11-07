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
        cur = root
        pre = None
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            cur = stack[-1]
            if (cur.left is None and cur.right is None) or (
                    pre is not None and (pre == cur.left or pre == cur.right)):
                res.append(stack.pop().val)
                pre = cur
            else:
                if cur.left is not None:
                    stack.append(cur.left)
                if cur.right is not None:
                    stack.append(cur.right)

        return res

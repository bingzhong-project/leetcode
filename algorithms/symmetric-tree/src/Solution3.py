# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        a_queue = []
        b_queue = []
        if root is not None:
            a_queue.append(root)
            b_queue.append(root)
        while len(a_queue) > 0 and len(b_queue) > 0:
            a_node = a_queue.pop(0)
            b_node = b_queue.pop(0)
            if a_node is not None:
                a_queue.append(a_node.left)
                a_queue.append(a_node.right)
            if b_node is not None:
                b_queue.append(b_node.right)
                b_queue.append(b_node.left)
            if a_node is None and b_node is None:
                continue
            if (a_node is None and b_node is not None) or (
                    a_node is not None
                    and b_node is None) or (a_node.val != b_node.val):
                return False

        return True

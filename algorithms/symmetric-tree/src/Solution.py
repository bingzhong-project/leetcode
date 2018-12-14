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

        def symmetric(paths):
            i, j = 0, len(paths) - 1
            while i <= j:
                if paths[i] != paths[j]:
                    return False
                i += 1
                j -= 1

            return True

        res = True
        if root is None:
            return res
        queue = list()
        queue.append(root)
        last = queue[-1]
        paths = list()
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
                paths.append(node.left.val)
            else:
                paths.append(-1)
            if node.right is not None:
                queue.append(node.right)
                paths.append(node.right.val)
            else:
                paths.append(-1)
            if node == last:
                if symmetric(paths):
                    paths = list()
                else:
                    res = False
                    break
                last = queue[-1] if len(queue) > 0 else None
        return res

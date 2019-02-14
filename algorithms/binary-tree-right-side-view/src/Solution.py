# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        if root is None:
            return result
        queue = list()
        queue.append(root)
        last_node = root
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if last_node == node:
                result.append(last_node.val)
                last_node = queue[len(queue) - 1] if queue else None
        return result

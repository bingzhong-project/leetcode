# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def traverse(node):
            node.visited = False
            if node.left is not None:
                node.left.parent = node
                traverse(node.left)
            if node.right is not None:
                node.right.parent = node
                traverse(node.right)

        root.parent = None
        traverse(root)

        queue = list()
        queue.append(target)
        layer = 0

        while queue:
            if layer == K:
                return [e.val for e in queue]
            layer += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                node.visited = True
                for vertex in (node.left, node.right, node.parent):
                    if vertex is not None and not vertex.visited:
                        queue.append(vertex)

        return []

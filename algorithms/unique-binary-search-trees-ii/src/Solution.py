# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_tress = generate_trees(i + 1, end)
                for l in left_trees:
                    for r in right_tress:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        all_trees.append(node)

            return all_trees

        return generate_trees(1, n) if n > 0 else []

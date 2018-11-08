# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(node, target, result, results):
            if node is not None:
                if node.left is None and node.right is None:
                    if target - node.val == 0:
                        results.append(result + [node.val])
                else:
                    dfs(node.left, target - node.val, result + [node.val],
                        results)
                    dfs(node.right, target - node.val, result + [node.val],
                        results)

        results = []
        dfs(root, sum, [], results)

        return results

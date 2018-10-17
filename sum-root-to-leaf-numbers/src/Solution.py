# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, paths, nums):
            if node is not None:
                if node.left is None and node.right is None:
                    num = 0
                    for path in paths:
                        num = num * 10 + path
                    num = num * 10 + node.val
                    nums.append(num)
                else:
                    dfs(node.left, paths + [node.val], nums)
                    dfs(node.right, paths + [node.val], nums)

        nums = []
        dfs(root, [], nums)
        return sum(nums)

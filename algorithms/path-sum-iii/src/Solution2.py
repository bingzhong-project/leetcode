import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        def func(node, cumulative_sum, target, counts):
            if node is None:
                return 0
            cumulative_sum += node.val
            ans = counts[cumulative_sum - target]
            counts[cumulative_sum] += 1
            ans += (func(node.left, cumulative_sum, target, counts) + func(
                node.right, cumulative_sum, target, counts))
            counts[cumulative_sum] -= 1
            return ans
        counts = collections.defaultdict(int)
        counts[0] = 1
        return func(root, 0, sum, counts)

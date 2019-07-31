# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if len(nums) == 0:
            return None
        max_val = max(nums)
        max_index = nums.index(max_val)
        left_node = self.constructMaximumBinaryTree(nums[:max_index])
        right_node = self.constructMaximumBinaryTree(nums[max_index + 1:])
        root = TreeNode(max_val)
        root.left = left_node
        root.right = right_node

        return root

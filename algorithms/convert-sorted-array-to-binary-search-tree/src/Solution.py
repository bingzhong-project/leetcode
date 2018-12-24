# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def construct(array, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(array[mid])
            node.left = construct(array, left, mid - 1)
            node.right = construct(array, mid + 1, right)
            return node

        return construct(nums, 0, len(nums) - 1)

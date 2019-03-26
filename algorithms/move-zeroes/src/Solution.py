class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 0
        while start < len(nums) and nums[start] != 0:
            start += 1
        end = start
        while end < len(nums) - 1:
            end += 1
            if nums[end] != 0:
                nums[start] = nums[end]
                nums[end] = 0
                start += 1

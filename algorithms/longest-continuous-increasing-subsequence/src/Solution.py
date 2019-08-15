class Solution:
    def findLengthOfLCIS(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        res = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                length = 1
            res = max(length, res)
        return res

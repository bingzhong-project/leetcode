class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        res = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1 and ones == 0:
                ones += 1
            elif nums[i] == 1 and nums[i - 1] == 1:
                ones += 1
            else:
                ones = 0
            res = max(ones, res)
        return res

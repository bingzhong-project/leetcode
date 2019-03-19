class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1, 0, -1):
            res[i - 1] = res[i] * nums[i]
        left = 1
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
        return res

class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        res = [0 for _ in range(len(nums))]
        prev_product = [1 for _ in range(len(nums))]
        back_product = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            prev_product[i + 1] = prev_product[i] * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            back_product[i - 1] = back_product[i] * nums[i]
        for i in range(len(nums)):
            res[i] = prev_product[i] * back_product[i]

        return res

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = [0 for _ in range(len(nums))]
        min_product = [0 for _ in range(len(nums))]
        result = max_product[0] = min_product[0] = nums[0]
        for i in range(1, len(nums)):
            max_product[i] = max(
                max(max_product[i - 1] * nums[i],
                    min_product[i - 1] * nums[i]), nums[i])
            min_product[i] = min(
                min(max_product[i - 1] * nums[i],
                    min_product[i - 1] * nums[i]), nums[i])
            result = max(result, max_product[i])
        return result

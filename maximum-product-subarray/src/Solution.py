class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -2**31
        nums_len = len(nums)
        dp = [[0 for _ in range(nums_len)] for _ in range(nums_len)]
        for i in range(nums_len):
            for j in range(i, nums_len):
                if i == j:
                    dp[i][j] = nums[i]
                elif j - i == 1:
                    dp[i][j] = nums[i] * nums[j]
                else:
                    dp[i][j] = dp[i][j - 1] * nums[j]
                result = max(result, dp[i][j])
        return result

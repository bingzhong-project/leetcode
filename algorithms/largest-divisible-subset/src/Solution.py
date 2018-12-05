class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        max_index = 0
        dp = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j][:]
                    dp[i].append(nums[i])
                    if len(dp[i]) > len(dp[max_index]):
                        max_index = i
        return dp[max_index]

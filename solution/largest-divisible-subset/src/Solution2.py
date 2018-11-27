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
        subset_index = [0 for _ in range(len(nums))]
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    subset_index[i] = j
                    if dp[max_index] < dp[i]:
                        max_index = i
        res = []
        for i in range(len(subset_index) - 1, -1, -1):
            if i == max_index:
                res.append(nums[max_index])
                max_index = subset_index[max_index]

        return res

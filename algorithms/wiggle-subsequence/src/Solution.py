class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        diff = None
        for i in range(1, len(nums)):
            cur_diff = nums[i] - nums[i - 1]
            if diff is None:
                dp[i] = dp[i - 1] if cur_diff == 0 else dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + 1 if (diff < 0 and cur_diff > 0) or (
                    diff > 0 and cur_diff < 0) else dp[i - 1]
            if cur_diff != 0:
                diff = cur_diff

        return dp[-1]

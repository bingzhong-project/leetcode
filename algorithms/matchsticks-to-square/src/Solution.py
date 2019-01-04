class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(nums, target, index=0):
            if index == len(nums):
                return True

            for i in range(4):
                if target[i] - nums[index] < 0:
                    continue
                target[i] -= nums[index]
                if (dfs(nums, target, index + 1)):
                    return True
                target[i] += nums[index]
            return False

        if len(nums) < 4:
            return False
        nums_sum = sum(nums)
        if nums_sum % 4 != 0:
            return False
        nums.sort(reverse=True)
        return dfs(nums, [nums_sum // 4] * 4)

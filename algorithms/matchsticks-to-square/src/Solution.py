class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(nums, sides, index=0):
            if index == len(nums):
                return True

            for i in range(4):
                if sides[i] - nums[index] < 0:
                    return False
                sides[i] -= nums[index]
                if (dfs(nums, sides, index + 1)):
                    return True
                sides[i] += nums[index]
            return False

        if len(nums) < 4:
            return False
        nums_sum = sum(nums)
        if nums_sum % 4 != 0:
            return False
        nums.sort()
        return dfs(nums, [nums_sum // 4] * 4)

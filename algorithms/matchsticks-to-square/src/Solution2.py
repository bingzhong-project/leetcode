class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(res, nums, visited, target, side_index=0, side_sum=0, index=0):
            if res[0]:
                return
            if side_index == 4:
                res[0] = True
                return
            if side_sum == target:
                dfs(res, nums, visited, target, side_index + 1)

            for i in range(index, len(nums)):
                if visited[i]:
                    continue
                if nums[i] + side_sum <= target:
                    visited[i] = True
                    dfs(res, nums, visited, target, side_index,
                        side_sum + nums[i], i + 1)
                    visited[i] = False

        if len(nums) < 4:
            return False
        nums_sum = sum(nums)
        if nums_sum % 4 != 0:
            return False
        nums.sort()
        target = nums_sum // 4
        visited = [False for _ in range(len(nums))]
        res = [False]
        dfs(res, nums, visited, target)
        return res[0]

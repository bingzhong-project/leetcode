class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, result, results):
            if len(nums) == len(result):
                results.append(result)
                return
            for i in range(len(nums)):
                if nums[i] not in result:
                    dfs(nums, result + [nums[i]], results)

        results = []
        dfs(nums, [], results)

        return results

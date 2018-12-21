class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, path, results):
            if len(nums) == len(path):
                results.append(path)
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    dfs(nums, path + [nums[i]], results)

        results = []
        dfs(nums, [], results)

        return results

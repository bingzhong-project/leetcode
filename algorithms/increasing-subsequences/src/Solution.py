class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, index, path, res):
            if len(path) > 1:
                res.append(path)
            used = set()
            for i in range(index, len(nums)):
                if nums[i] in used:
                    continue
                if len(path) > 0 and path[-1] > nums[i]:
                    continue
                used.add(nums[i])
                dfs(nums, i + 1, path + [nums[i]], res)

        res = []
        dfs(nums, 0, [], res)

        return res

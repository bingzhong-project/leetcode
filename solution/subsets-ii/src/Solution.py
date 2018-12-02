class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, index, path, res):
            if path not in res:
                res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, path + [nums[i]], res)

        res = []
        dfs(sorted(nums), 0, [], res)
        return res

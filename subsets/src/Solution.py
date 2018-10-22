class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, level, path, res):
            if level == len(nums):
                return
            for i in range(len(nums)):
                num = nums[i]
                if num in path:
                    continue
                if len(path) > 0 and (num < path[-1] or num < path[0]):
                    continue
                path.append(num)
                res.append(path[:])
                dfs(nums, level + 1, path, res)
                path.pop()

        res = []
        dfs(nums, 0, [], res)
        res.append([])

        return res

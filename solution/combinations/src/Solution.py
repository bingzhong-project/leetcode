class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(nums, n, k, index, path, res):
            if len(path) == k:
                res.append(path)
                return
            for i in range(index, len(nums)):
                tmp = path[:]
                tmp.append(nums[i])
                dfs(nums, n, k, i + 1, tmp, res)
                if len(tmp) + (n - i) < k:
                    return

        res = []
        dfs([i for i in range(1, n + 1)], n, k, 0, [], res)

        return res

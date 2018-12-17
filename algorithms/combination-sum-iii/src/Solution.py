class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(target, k, start, paths, res):
            if k == 0:
                if target == 0:
                    res.append(paths)
                return
            for i in range(start, 10):
                if target - i >= 0 and k - 1 >= 0:
                    dfs(target - i, k - 1, i + 1, paths + [i], res)

        res = []
        dfs(n, k, 1, [], res)
        return res

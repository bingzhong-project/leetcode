class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, target, start, result, results):
            if target == 0:
                results.append(result)
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate <= target:
                    dfs(candidates, target - candidate, i,
                        result + [candidate], results)

        results = []
        dfs(sorted(candidates), target, 0, [], results)
        return results

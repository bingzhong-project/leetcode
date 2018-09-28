class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, target, start, result, results):
            if target == 0:
                if result not in results:
                    results.append(result)
                return
            for i in range(start, len(candidates)):
                if target < candidates[i]:
                    continue
                dfs(candidates, target - candidates[i], i + 1,
                    result + [candidates[i]], results)

        results = []
        dfs(sorted(candidates), target, 0, [], results)
        return results

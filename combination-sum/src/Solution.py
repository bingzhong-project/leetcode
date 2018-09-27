class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, target, candidate_sum, result, results):
            if candidate_sum == target:
                result = sorted(result)
                if result not in results:
                    results.append(result)
                return
            for i in range(len(candidates)):
                candidate = candidates[i]
                if candidate_sum + candidate <= target:
                    result.append(candidate)
                    dfs(candidates, target, candidate_sum + candidate,
                        result[:], results)
                    result.pop()

        results = []
        dfs(candidates, target, 0, [], results)
        return results

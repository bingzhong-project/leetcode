class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, target, candidate_sum, result, results):
            if candidate_sum == target:
                results.append(result)
                return
            for i in range(len(candidates)):
                candidate = candidates[i]
                if candidate_sum + candidate <= target:
                    result.append(candidate)
                    candidate_sum += candidate
                    dfs(candidates, target, candidate_sum, result[:], results)

        results = []
        dfs(candidates, target, 0, [], results)
        return results


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))

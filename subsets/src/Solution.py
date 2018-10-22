class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, times, result, results):
            if times == len(nums):
                return
            for i in range(len(nums)):
                num = nums[i]
                if num in result:
                    continue
                if len(result) > 0 and num < result[-1]:
                    continue
                result.append(num)
                if num < result[0]:
                    result.pop()
                    continue
                if result in results:
                    result.pop()
                    continue
                else:
                    results.append(result[:])
                dfs(nums, times + 1, result, results)
                result.pop()

        results = []
        dfs(nums, 0, [], results)
        results.append([])

        return results

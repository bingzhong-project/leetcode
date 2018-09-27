class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, result, results):
            if len(nums) == len(result):
                results.append(result)
                return
            for i in range(len(nums)):
                if nums[i] not in result:
                    result.append(nums[i])
                    dfs(nums, result[:], results)
                    result.pop()

        results = []
        dfs(nums, [], results)
        # def validate(num, n, result, results):
        #     for i in range(n):
        #         if result[i] == num:
        #             return False
        #     return True

        # def dfs(nums, n, result, results):
        #     if len(nums) == n:
        #         results.append(result)
        #         return
        #     for i in range(len(nums)):
        #         result[n] = nums[i]
        #         if validate(nums[i], n, result, results):
        #             dfs(nums, n + 1, result[:], results)

        # results = []
        # dfs(nums, 0, [-1 for i in range(len(nums))], results)

        return results

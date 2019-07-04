class Solution:
    def arrayNesting(self, nums: 'List[int]') -> 'int':
        def func(array, i, memo, visited):
            if array[i] in visited:
                return 0
            if i in memo:
                return memo[i]
            visited.add(array[i])
            count = func(array, array[i], memo, visited) + 1
            memo[i] = count
            return count

        res = 0
        memo = {}
        for i in range(len(nums)):
            res = max(res, func(nums, i, memo, set()))

        return res

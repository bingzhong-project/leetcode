class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        """回溯算法 TLE

        Returns:
            bool: 答案
        """

        def func(nums, elements, index, visited, res):
            amount = sum(elements)
            if amount == sum(nums) - amount:
                res[0] = True
                return
            for i in range(index, len(nums)):
                new_elements = elements + [nums[i]]
                amount = sum(new_elements)
                if amount not in visited:
                    visited.add(amount)
                    func(nums, new_elements, i + 1, visited, res)

        res = [False]
        func(nums, [], 0, set(), res)
        return res[0]

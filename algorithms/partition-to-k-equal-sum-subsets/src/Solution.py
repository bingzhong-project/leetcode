class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: 'int') -> 'bool':
        def func(nums, index, cur_sum, target, k, visited):
            if k == 1:
                return True
            if cur_sum == target:
                return func(nums, 0, 0, target, k - 1, visited)
            for i in range(index, len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                if (func(nums, i + 1, cur_sum + nums[i], target, k, visited)):
                    return True
                visited[i] = False

            return False

        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        target = nums_sum // k
        return func(nums, 0, 0, target, k, [False for _ in range(len(nums))])

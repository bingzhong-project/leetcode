class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        def func(nums, target, index):
            if target == 0:
                return True
            if target < 0:
                return False
            for i in range(index, len(nums)):
                if target - nums[i] < 0:
                    break
                if func(nums, target - nums[i], i + 1):
                    return True

            return False

        target = sum(nums)
        if target % 2 != 0:
            return False
        nums.sort(reverse=True)
        return func(nums, target // 2, 0)

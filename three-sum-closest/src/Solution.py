class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = 2**31
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == target:
                    return target
                if three_sum > target:
                    right -= 1
                else:
                    left += 1
                if abs(target - result) > abs(target - three_sum):
                    result = three_sum
        return result

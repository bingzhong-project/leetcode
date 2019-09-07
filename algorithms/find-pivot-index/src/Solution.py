class Solution:
    def pivotIndex(self, nums: list) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i

        return -1
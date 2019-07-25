class Solution:
    def findMaxAverage(self, nums: 'List[int]', k: 'int') -> 'float':
        if len(nums) < k:
            return float(0)
        nums_sum = sum(nums[:k])
        max_sum = nums_sum
        left = 0
        right = k - 1
        while right < len(nums) - 1:
            nums_sum -= nums[left]
            nums_sum += nums[right + 1]
            max_sum = max(max_sum, nums_sum)
            left += 1
            right += 1
        return max_sum / k

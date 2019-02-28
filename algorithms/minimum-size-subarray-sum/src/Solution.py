class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        res = 2**31
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if res == 2**31 else res

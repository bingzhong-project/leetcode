class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        def binary(left, right, key, sums):
            while left <= right:
                mid = (left + right) // 2
                if sums[mid] >= key:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        res = len(nums) + 1
        sums = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            sums[i] += sums[i - 1] + nums[i - 1]
        for i in range(len(nums) + 1):
            right = binary(i + 1, len(nums), sums[i] + s, sums)
            if right == len(nums) + 1:
                break
            res = min(res, right - i)

        return 0 if res == len(nums) + 1 else res

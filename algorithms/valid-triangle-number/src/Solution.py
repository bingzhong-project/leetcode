class Solution:
    def triangleNumber(self, nums: 'List[int]') -> 'int':
        res = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = nums[i] + nums[j]
                left = j + 1
                right = len(nums)
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                res += (right - 1 - j)
        return res

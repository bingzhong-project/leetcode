class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> 'int':
        sort_nums = sorted(nums)
        left = None
        right = None
        for i in range(len(nums)):
            if nums[i] != sort_nums[i]:
                if left is None:
                    left = i
                else:
                    right = i
        return 0 if left == right else right - left + 1

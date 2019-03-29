class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        if len(nums) < 2:
            return False
        left, right = 2**31, 2**31
        for i in range(len(nums)):
            if nums[i] < left:
                left = nums[i]
            elif nums[i] > left and nums[i] < right:
                right = nums[i]
            elif nums[i] > right:
                return True
        return False

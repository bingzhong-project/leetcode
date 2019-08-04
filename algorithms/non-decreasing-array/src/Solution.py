class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        decreasing = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if decreasing > 0:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                decreasing += 1
        return True

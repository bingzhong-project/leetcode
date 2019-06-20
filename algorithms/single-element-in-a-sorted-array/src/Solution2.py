class Solution:
    def singleNonDuplicate(self, nums: 'List[int]') -> 'int':
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if right - left == 2:
                return nums[left] if nums[mid] == nums[right] else nums[right]
            if nums[mid] == nums[mid - 1]:
                if len(nums[:mid + 1]) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if len(nums[:mid]) % 2 == 0:
                    left += 2
                else:
                    right -= 1
            else:
                return nums[mid]
        return nums[left]

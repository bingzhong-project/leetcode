class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary(left, right, nums, target):
            if right - left == 1 or left == right:
                if target > nums[right]:
                    return right + 1
                if target == nums[left]:
                    return left
                if target == nums[right]:
                    return right
                if target < nums[left]:
                    return left - 1
                if target > nums[left]:
                    return left + 1
            mid = (left + right) // 2
            if nums[mid] > target:
                return binary(left, mid, nums, target)
            elif nums[mid] < target:
                return binary(mid, right, nums, target)
            else:
                return mid

        if len(nums) == 0:
            return 0
        result = binary(0, len(nums) - 1, nums, target)
        return 0 if result < 0 else result

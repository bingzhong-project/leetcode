class Solution:
    def search(self, nums: list, target: int) -> int:
        def binary(nums, target, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] > target:
                return binary(nums, target, left, mid - 1)
            elif nums[mid] < target:
                return binary(nums, target, mid + 1, right)
            else:
                return mid

        return binary(nums, target, 0, len(nums) - 1)

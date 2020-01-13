class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = (k + len(nums)) % len(nums)
        count = 0
        for start in range(len(nums)):
            if count >= len(nums):
                break
            index = start
            num = nums[start]
            while True:
                cursor = (index + len(nums) + k) % len(nums)
                temp = nums[cursor]
                nums[cursor] = num
                num = temp
                index = cursor
                count += 1
                if start == cursor:
                    break

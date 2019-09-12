class Solution:
    def dominantIndex(self, nums: list) -> int:
        first_max = nums[0]
        second_max = -1
        index = 0
        for i in range(1, len(nums)):
            if nums[i] > first_max:
                second_max = first_max
                first_max = nums[i]
                index = i
            elif nums[i] > second_max:
                second_max = nums[i]

        return -1 if first_max < second_max * 2 else index

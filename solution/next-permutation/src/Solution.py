class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        cursor = 0
        not_continue_flag = True
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                cursor = i - 1
                not_continue_flag = False
                break
        if not_continue_flag:
            nums.sort()
            return
        for i in range(cursor + 1, len(nums) + 1):
            if i == len(nums) or nums[cursor] >= nums[i]:
                tmp = nums[i - 1]
                nums[i - 1] = nums[cursor]
                nums[cursor] = tmp
                break
        front_array = nums[:cursor + 1]
        tail_array = sorted(nums[cursor + 1:])
        new_nums = front_array + tail_array
        for i in range(len(nums)):
            nums[i] = new_nums[i]

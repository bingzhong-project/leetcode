class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = False
        cur_position = 0
        while cur_position < len(nums):
            num = nums[cur_position]
            if num == 0 and cur_position != len(nums) - 1:
                break
            if num + cur_position >= len(nums) - 1:
                result = True
                break
            position_num = -1
            add_position_num = 0
            for i in range(1, num + 1):
                if position_num <= nums[cur_position + i]:
                    add_position_num = i
                    position_num = nums[cur_position + i]
            cur_position += add_position_num

        return result

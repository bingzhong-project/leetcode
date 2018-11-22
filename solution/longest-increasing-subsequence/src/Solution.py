class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def lis(index, nums, max_lengths):
            if index == len(nums) - 1:
                max_lengths[index] = 1
                return
            if max_lengths[index + 1] == 0:
                lis(index + 1, nums, max_lengths)
            for i in range(index + 1, len(max_lengths)):
                if nums[index] < nums[i]:
                    max_lengths[index] = max(max_lengths[index],
                                             max_lengths[i] + 1)
            if max_lengths[index] == 0:
                max_lengths[index] = 1

        if len(nums) == 0:
            return 0

        max_lengths = [0 for _ in range(len(nums))]
        lis(0, nums, max_lengths)
        return max(max_lengths)

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def sub_rob(houses):
            max_steal = 0
            max_not_steal = 0
            for i in range(len(houses)):
                if i == 0:
                    max_steal = houses[i]
                    max_not_steal = 0
                else:
                    temp = max_steal
                    max_steal = max_not_steal + houses[i]
                    max_not_steal = max(temp, max_not_steal)
            return max(max_steal, max_not_steal)

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(sub_rob(nums[:len(nums) - 1]), sub_rob(nums[1:]))

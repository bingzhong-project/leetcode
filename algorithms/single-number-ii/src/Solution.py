class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0
        b = 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b

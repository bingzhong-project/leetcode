class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cumsum = 0
        record = {0: -1}
        maxlen = 0
        for i in range(len(nums)):
            cumsum += -1 if nums[i] == 0 else 1
            if cumsum in record:
                maxlen = max(maxlen, i - record[cumsum])
            else:
                record[cumsum] = i
        return maxlen

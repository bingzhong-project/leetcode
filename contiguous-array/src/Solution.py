class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cumulate_sum = 0
        record = {0: -1}
        maxlen = 0
        for i in range(len(nums)):
            cumulate_sum += -1 if nums[i] == 0 else 1
            if cumulate_sum in record:
                maxlen = max(maxlen, i - record[cumulate_sum])
            else:
                record[cumulate_sum] = i
        return maxlen

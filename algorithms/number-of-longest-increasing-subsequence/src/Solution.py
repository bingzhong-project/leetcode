class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        length = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]
        max_count = 0
        max_length = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if length[i] == length[j] + 1:
                    count[i] += count[j]
                elif length[i] < length[j] + 1:
                    length[i] = length[j] + 1
                    count[i] = count[j]
            if length[i] == max_length:
                max_count += count[i]
            elif max_length < length[i]:
                max_count = count[i]
                max_length = length[i]

        return max_count

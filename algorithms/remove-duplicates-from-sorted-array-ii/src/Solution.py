class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        start = end = 0
        length = len(nums)
        while end < length - 1:
            while end + 1 < length and nums[end] == nums[end + 1]:
                end += 1
            if end - start > 1:
                dc = end - start - 1
                for i in range(start, length):
                    if i + dc < length:
                        nums[i] = nums[i + dc]
                start = start + 2 if nums[start] == nums[start
                                                         + 1] else start + 1
                end = start
                length -= dc
            else:
                end += 1
                start = end
        return length

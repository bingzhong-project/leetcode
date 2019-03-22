class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        res = []
        start, end = 0, 0
        while end < len(nums):
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end += 1
            res.append(
                str(nums[start]) if start == end else '%s->%s' % (nums[start],
                                                                  nums[end]))
            end += 1
            start = end
        return res

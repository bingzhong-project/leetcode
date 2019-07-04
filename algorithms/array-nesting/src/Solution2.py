class Solution:
    def arrayNesting(self, nums: 'List[int]') -> 'int':
        res = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            length = 0
            j = i
            while nums[j] != -1:
                length += 1
                pre = j
                j = nums[j]
                nums[pre] = -1
            res = max(res, length)
        return res

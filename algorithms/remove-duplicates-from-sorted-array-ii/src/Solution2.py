class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        length = len(nums)
        if length <= 2:
            return length
        left, right = 1, 2
        while right < length:
            if nums[left] == nums[right] and nums[right] == nums[left - 1]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left + 1

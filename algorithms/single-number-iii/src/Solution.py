class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff

        a = 0
        b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        return [a, b]

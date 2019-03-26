class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        major1 = None
        major2 = None
        count1 = 0
        count2 = 0
        for n in nums:
            if major1 == n:
                count1 += 1
            elif major2 == n:
                count2 += 1
            elif count1 == 0:
                major1 = n
                count1 = 1
            elif count2 == 0:
                major2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        count1 = 0
        count2 = 0
        k = len(nums) // 3
        for n in nums:
            if n == major1:
                count1 += 1
                if count1 == k + 1:
                    res.append(n)
            if n == major2:
                count2 += 1
                if count2 == k + 1:
                    res.append(n)
        return res

class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        marjor1 = None
        marjor2 = None
        count1 = 0
        count2 = 0
        for n in nums:
            if marjor1 == n:
                count1 += 1
            elif marjor2 == n:
                count2 += 1
            elif count1 == 0:
                marjor1 = n
                count1 = 1
            elif count2 == 0:
                marjor2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        count1 = 0
        count2 = 0
        k = len(nums) // 3
        for n in nums:
            if n == marjor1:
                count1 += 1
                if count1 == k + 1:
                    res.append(n)
            if n == marjor2:
                count2 += 1
                if count2 == k + 1:
                    res.append(n)
        return res

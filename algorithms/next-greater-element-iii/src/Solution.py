import collections


class Solution:
    def nextGreaterElement(self, n: 'int') -> 'int':
        nums = []
        pos = collections.defaultdict(list)
        div = n
        index = 0
        while div > 0:
            div, mod = divmod(div, 10)
            nums.append(mod)
            pos[mod].append(index)
            index += 1

        gi = 2**31
        li = 2**31

        for num in sorted(list(pos.keys())):
            for i in range(num - 1, -1, -1):
                if i in pos:
                    for j in pos[i]:
                        temp_gi = pos[num][0]
                        temp_li = j
                        if temp_gi < temp_li and temp_li < li:
                            gi = temp_gi
                            li = temp_li
        if gi == li:
            return -1
        temp = nums[gi]
        nums[gi] = nums[li]
        nums[li] = temp

        nums = sorted(nums[:li], reverse=True) + nums[li:]

        res = 0

        for num in nums[::-1]:
            res = res * 10 + num

        return res if res < 2**31 else -1

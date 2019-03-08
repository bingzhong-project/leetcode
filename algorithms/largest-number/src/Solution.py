class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        strs = [str(num) for num in nums]
        strs = sorted(strs, key=LargerNumKey)
        return "0" if strs[0] == '0' else "".join(strs)

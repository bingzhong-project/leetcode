class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        res = 0
        ans = x ^ y
        while ans:
            if ans & 1 == 1:
                res += 1
            ans >>= 1
        return res

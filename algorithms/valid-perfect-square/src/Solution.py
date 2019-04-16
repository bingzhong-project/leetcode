class Solution:
    def isPerfectSquare(self, num: 'int') -> 'bool':
        if num == 1:
            return True
        left = 1
        right = num
        while left < right - 1:
            mid = (left + right) // 2
            if mid**2 > num:
                right = mid
            elif mid**2 < num:
                left = mid
            else:
                return True
        return False

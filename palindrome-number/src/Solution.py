class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        prototype = x
        if (x < 0):
            return False
        else:
            res = 0
            while x != 0:
                num = int(x % 10)
                res = int(res * 10 + num)
                x = int(x / 10)
            return res == prototype

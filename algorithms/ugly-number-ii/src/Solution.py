class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list()
        dp.append(1)
        i1 = 0
        i2 = 0
        i3 = 0
        while len(dp) < n:
            num1 = dp[i1] * 2
            num2 = dp[i2] * 3
            num3 = dp[i3] * 5
            num = min(num1, num2, num3)
            if num == num1:
                i1 += 1
            if num == num2:
                i2 += 1
            if num == num3:
                i3 += 1
            dp.append(num)
        return dp[-1]

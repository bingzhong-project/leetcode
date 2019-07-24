class Solution:
    def minSteps(self, n: 'int') -> 'int':
        def find_factor(num):
            for i in range(2, num // 2 + 1):
                div, mod = divmod(num, i)
                if mod == 0:
                    return [i, div]
            return [1, num]

        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factor = find_factor(i)
            step = 0
            for num in factor:
                step += (dp[num] if num == 1 or dp[num] > 0 else num)
            dp[i] = step

        return dp[-1]

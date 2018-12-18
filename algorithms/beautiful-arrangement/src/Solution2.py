class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def dfs(pos, numbers, cache={}):
            if pos == 1:
                return 1
            key = (pos, numbers)
            if key in cache:
                return cache[key]
            total = 0
            for i, number in enumerate(numbers):
                if number % pos == 0 or pos % number == 0:
                    total += dfs(pos - 1, numbers[:i] + numbers[i + 1:], cache)
            cache[(pos, numbers)] = total
            return total

        return dfs(N, tuple([i for i in range(1, N + 1)]))

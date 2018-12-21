class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def dfs(numbers, i, res):
            if len(numbers) == 0:
                res[0] += 1
            for pos, number in enumerate(numbers):
                if number % i == 0 or i % number == 0:
                    dfs(numbers[:pos] + numbers[pos + 1:], i + 1, res)

        numbers = [n for n in range(1, N + 1)]
        res = [0]
        dfs(numbers, 1, res)
        return res[0]

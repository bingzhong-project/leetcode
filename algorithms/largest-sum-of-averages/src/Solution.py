class Solution:
    def largestSumOfAverages(self, A: list, K: int) -> float:
        def avg(array, start, end, cache):
            if (start, end) in cache:
                return cache[(start, end)]
            else:
                average = sum(array[start:end]) / len(array[start:end])
                cache[(start, end)] = average
                return average

        def func(array, index, k, memo, cache):
            if index == len(array):
                return 0
            if k == 1:
                return avg(array, index, len(array), cache)
            if (index, k) in memo:
                return memo[(index, k)]
            res = 0
            for i in range(index, len(array)):
                average = avg(array, index, i + 1, cache)
                res = max(res,
                          average + func(array, i + 1, k - 1, memo, cache))
            memo[(index, k)] = res
            return res

        return func(A, 0, K, {}, {})

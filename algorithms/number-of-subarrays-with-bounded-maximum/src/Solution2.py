class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        def count(arr, bound):
            res = 0
            cur = 0
            start = 0
            for end in range(len(arr)):
                if arr[end] <= bound:
                    cur += end - start + 1
                else:
                    res += cur
                    cur = 0
                    start = end + 1
            return res + cur

        return count(A, R) - count(A, L - 1)

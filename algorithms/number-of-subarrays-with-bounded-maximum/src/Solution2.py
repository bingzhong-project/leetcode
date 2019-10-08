class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        def count(arr, bound):
            res = 0
            cur = 0
            for num in arr:
                cur = cur + 1 if num <= bound else 0
                res += cur
            return res

        return count(A, R) - count(A, L - 1)

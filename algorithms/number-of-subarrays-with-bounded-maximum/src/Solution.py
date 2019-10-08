class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        """TLE
        """
        res = 0
        for i in range(len(A)):
            if A[i] > R:
                continue
            cur_max = 2**-31
            for j in range(i, len(A)):
                cur_max = max(cur_max, A[j])
                if cur_max > R:
                    continue
                if cur_max >= L:
                    res += 1
        return res

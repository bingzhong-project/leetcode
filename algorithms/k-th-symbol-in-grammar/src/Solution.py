class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def func(n, k, reverse):
            if n == 1:
                return 1 if reverse else 0
            pre_len = 2**(n - 2)
            return func(n - 1, k - pre_len,
                        not reverse) if k > pre_len else func(
                            n - 1, k, reverse)

        return func(N, K, False)

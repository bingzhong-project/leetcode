class Solution:
    def minSwap(self, A: list, B: list) -> int:
        n = len(A)
        swap = [2**31 for _ in range(n)]
        no_swap = [2**31 for _ in range(n)]
        swap[0] = 1
        no_swap[0] = 0

        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap[i] = swap[i - 1] + 1
                no_swap[i] = no_swap[i - 1]
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap[i] = min(no_swap[i - 1] + 1, swap[i])
                no_swap[i] = min(swap[i - 1], no_swap[i])

        return min(swap[-1], no_swap[-1])

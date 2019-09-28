class Solution:
    def isIdealPermutation(self, A: list) -> bool:
        min_num = 2**31
        for i in range(len(A) - 1, 1, -1):
            min_num = min(min_num, A[i])
            if min_num < A[i - 2]:
                return False

        return True

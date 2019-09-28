class Solution:
    def isIdealPermutation(self, A: list) -> bool:
        if len(A) <= 2:
            return True
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True

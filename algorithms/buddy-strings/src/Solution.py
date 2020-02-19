class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        a_set = set(A)
        b_set = set(B)
        if len(a_set) != len(b_set):
            return False
        if A == B:
            return len(a_set) < len(A)
        array = []
        for i in range(len(A)):
            if A[i] != B[i]:
                array.append(i)

        if len(array) != 2:
            return False
        return A[array[0]] == B[array[1]] and A[array[1]] == B[array[0]]

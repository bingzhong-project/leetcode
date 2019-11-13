class Solution:
    def shiftingLetters(self, S: str, shifts: list) -> str:
        sum_shift = sum(shifts)
        for i in range(len(shifts)):
            temp = shifts[i]
            shifts[i] = sum_shift
            sum_shift -= temp

        res = ""
        for i in range(len(S)):
            res += chr(((ord(S[i]) - ord('a') + shifts[i]) % 26) + ord('a'))

        return res

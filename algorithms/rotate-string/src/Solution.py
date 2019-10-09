class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        ai = 0
        bi = 0
        count = 0
        equal = False
        while count < len(A) * 2:
            if A[ai % len(A)] != B[bi]:
                bi = 0
                if equal:
                    ai -= 1
                equal = False
            else:
                if bi == len(B) - 1:
                    return True
                bi += 1
                equal = True
            ai += 1
            count += 1

        return False


if __name__ == "__main__":
    print(Solution().rotateString("bbbacddceeb", "ceebbbbacdd"))

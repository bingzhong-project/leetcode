class Solution:
    def largeGroupPositions(self, S: str) -> list:
        res = []
        pre = ""
        for i in range(len(S)):
            if S[i] == pre:
                continue
            count = 1
            for j in range(i + 1, len(S)):
                if S[i] == S[j]:
                    count += 1
                else:
                    j -= 1
                    break
            if count >= 3:
                res.append([i, j])
            pre = S[i]

        return res

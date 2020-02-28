class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        array = [0 for _ in range(len(d))]
        for i in range(len(s)):
            for j in range(len(d)):
                if array[j] < len(d[j]):
                    if s[i] == d[j][array[j]]:
                        array[j] += 1

        res = ""
        for i in range(len(d)):
            if len(d[i]) != array[i]:
                continue
            if len(res) == array[i]:
                res = min(d[i], res)
            else:
                res = d[i] if array[i] > len(res) else res

        return res

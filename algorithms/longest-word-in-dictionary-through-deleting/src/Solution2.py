class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        def is_sequence(x, y):
            i = 0
            for c in x:
                if c == y[i]:
                    i += 1
                    if i == len(y):
                        return True
            return False

        res = ""
        for word in d:
            if is_sequence(s, word):
                if len(res) == len(word):
                    res = min(res, word)
                else:
                    res = word if len(word) > len(res) else res

        return res

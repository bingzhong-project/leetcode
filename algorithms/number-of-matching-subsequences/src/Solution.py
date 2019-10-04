class Solution:
    def numMatchingSubseq(self, S: str, words: list) -> int:
        """TLE
        """
        def is_sub_seq(word1, word2):
            i = 0
            j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    j += 1
                i += 1
            return j == len(word2)

        res = 0
        memo = {}
        for word in words:
            if word in memo:
                if memo[word]:
                    res += 1
            else:
                memo[word] = is_sub_seq(S, word)
                if memo[word]:
                    res += 1

        return res

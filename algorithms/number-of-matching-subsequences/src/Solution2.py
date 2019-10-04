import collections


class Solution:
    def numMatchingSubseq(self, S: str, words: list) -> int:
        memo = collections.defaultdict(list)
        for i in range(len(words)):
            word = words[i]
            memo[word[0]] += [(i, 1)]

        res = 0
        for s in S:
            if s not in memo:
                continue
            pos = memo[s]
            del memo[s]
            for index, next_index in pos:
                if next_index >= len(words[index]):
                    res += 1
                else:
                    memo[words[index][next_index]] += [(index, next_index + 1)]

        return res

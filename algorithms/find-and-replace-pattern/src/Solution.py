import collections


class Solution:
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        res = []
        pattern_pos = collections.defaultdict(list)
        for i in range(len(pattern)):
            pattern_pos[pattern[i]] += [i]
        for word in words:
            word_post = collections.defaultdict(list)
            for i in range(len(word)):
                word_post[word[i]] += [i]
            flag = True
            for i in range(len(word)):
                if tuple(pattern_pos[pattern[i]]) != tuple(word_post[word[i]]):
                    flag = False
                    break
            if flag:
                res.append(word)
        return res

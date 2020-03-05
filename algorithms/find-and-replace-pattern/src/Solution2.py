class Solution:
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        def match(word, pattern):
            word_map = {}
            pattern_map = {}
            for i in range(len(pattern)):
                if pattern[i] not in pattern_map:
                    pattern_map[pattern[i]] = word[i]
                if word[i] not in word_map:
                    word_map[word[i]] = pattern[i]
                if (pattern_map[pattern[i]],
                        word_map[word[i]]) != (word[i], pattern[i]):
                    return False
            return True

        res = []
        for word in words:
            if match(word, pattern):
                res.append(word)
        return res

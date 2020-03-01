class Solution:
    def maxProduct(self, words: list) -> int:
        masks = [0 for _ in range(len(words))]
        for i in range(len(words)):
            word = words[i]
            mask = 0
            for char in word:
                mask |= 2**(ord(char) - ord('a'))
            masks[i] = mask
        res = 0
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i] & masks[j] == 0:
                    res = max(len(words[i]) * len(words[j]), res)

        return res

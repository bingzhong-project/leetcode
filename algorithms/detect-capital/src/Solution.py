class Solution:
    def detectCapitalUse(self, word: 'str') -> 'bool':
        def is_upper(word):
            return ord(word) >= ord('A') and ord(word) <= ord('Z')

        upper_count = 0
        for s in word:
            if is_upper(s):
                upper_count += 1
        if upper_count == len(word):
            return True
        elif upper_count == 0:
            return True
        elif upper_count < len(word):
            if upper_count == 1 and is_upper(word[0]):
                return True
            else:
                return False

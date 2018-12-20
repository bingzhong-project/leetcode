class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_dict = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        result = list(phone_dict[digits[0]])
        for i in range(len(digits)):
            cache = list()
            letters = phone_dict[digits[i]]
            if len(letters) > 0:
                for letter in letters:
                    for j in range(len(result)):
                        cache.append(result[j] + letter)
                result = cache
        return result

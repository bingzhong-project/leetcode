class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        pre_num = 0
        for roman_num in s:
            num = roman_dict[roman_num]
            if num > pre_num:
                num -= pre_num
                result -= pre_num
            result += num
            pre_num = num

        return result

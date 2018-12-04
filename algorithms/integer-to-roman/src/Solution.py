class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        result = ""
        factor = 1
        while num > 0:
            target_num = int(num % 10) * factor
            if target_num in roman_dict:
                result = roman_dict[target_num] + result
            else:
                tmp_res = ""
                same_times = 0
                while target_num > 0:
                    same_times += 1
                    if same_times == 4:
                        tmp_res = roman_dict[factor] + roman_dict[factor * (
                            same_times + 1)]
                    elif same_times == 5:
                        tmp_res = roman_dict[factor * same_times]
                    elif same_times == 9:
                        tmp_res = roman_dict[factor] + roman_dict[factor * (
                            same_times + 1)]
                    else:
                        tmp_res = tmp_res + roman_dict[factor]
                    target_num -= factor
                result = tmp_res + result
            num /= 10
            factor *= 10

        return result

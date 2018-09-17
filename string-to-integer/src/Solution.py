class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        result = list()
        is_start = False
        is_valid = False
        for s in str:
            if is_start:
                if s in num:
                    result.append(s)
                    is_valid = True
                else:
                    break
            else:
                if s == '-':
                    result.append(s)
                    is_start = True
                elif s == '+':
                    is_start = True
                elif s in num:
                    result.append(s)
                    is_valid = True
                    is_start = True
                    continue
                elif s == ' ':
                    continue
                else:
                    break
        res_num = 0
        if len(result) > 0 and is_valid:
            res_num = int("".join(result))
        if res_num < -2147483648:
            res_num = -2147483648
        elif res_num > 2147483647:
            res_num = 2147483647
        return res_num

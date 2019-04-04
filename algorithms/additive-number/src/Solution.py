class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def dfs(num, addend1, addend2):
            if (len(num) > 1 and num[0] == '0') or (len(addend1) > 1
                                                    and addend1[0] == '0') or (
                                                        len(addend2) > 1
                                                        and addend2[0] == '0'):
                return False
            sum_str = str(int(addend1) + int(addend2))
            if sum_str == num:
                return True
            if len(sum_str) >= len(num) or num[:len(sum_str)] != sum_str:
                return False
            return dfs(num[len(sum_str):], addend2, num[:len(sum_str)])

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                addend1 = num[:i]
                addend2 = num[i:j]
                if dfs(num[j:], addend1, addend2):
                    return True

        return False

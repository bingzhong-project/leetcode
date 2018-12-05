class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        str_len = len(s)
        result = list()
        for i in range(numRows):
            cursor = i
            while cursor < str_len:
                result.append(s[cursor])
                if i != 0 and i != numRows - 1:
                    red_cursor = cursor + (2 * numRows - 2) - 2 * i
                    if red_cursor < str_len:
                        result.append(s[red_cursor])
                cursor = cursor + (2 * numRows - 2)
        return "".join(result)

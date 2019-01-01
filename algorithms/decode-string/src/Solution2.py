class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0
        stack = [["", 1]]
        for string in s:
            if string.isdigit():
                num = num * 10 + int(string)
            elif string == "[":
                stack.append(["", num])
                num = 0
            elif string == "]":
                element = stack.pop()
                stack[-1][0] += element[0] * element[1]
            else:
                stack[-1][0] += string

        return stack[-1][0]

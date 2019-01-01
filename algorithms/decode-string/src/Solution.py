class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for string in s:
            if string == "]":
                tmp_str = ""
                while stack[-1] != "[":
                    tmp_str = stack.pop() + tmp_str
                stack.pop()
                tmp_num = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    tmp_num = stack.pop() + tmp_num
                stack.append(int(tmp_num) * tmp_str)
            else:
                stack.append(string)
        return "".join(stack)

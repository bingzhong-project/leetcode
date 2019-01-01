class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        left_bracket = "["
        right_bracket = "]"

        stack = []
        for string in s:
            if string == right_bracket:
                tmp_str = ""
                while stack[-1] != left_bracket:
                    tmp_str = stack.pop() + tmp_str
                stack.pop()
                tmp_num = ""
                while len(stack) > 0 and stack[-1] in nums:
                    tmp_num = stack.pop() + tmp_num
                tmp_res = int(tmp_num) * tmp_str
                stack.append(tmp_res)
            else:
                stack.append(string)
        return "".join(stack)

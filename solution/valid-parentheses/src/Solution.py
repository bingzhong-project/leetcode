class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {"(": 1, "[": 2, "{": 3, ")": -1, "]": -2, "}": -3}
        stack = []
        for p in s:
            if len(stack) == 0 and parentheses[p] < 0:
                return False
            if len(stack) > 0:
                top = stack[-1]
                if parentheses[top] + parentheses[p] == 0:
                    stack.pop()
                    continue
                if parentheses[top] * parentheses[p] < 0:
                    return False
            stack.append(p)
        return len(stack) == 0

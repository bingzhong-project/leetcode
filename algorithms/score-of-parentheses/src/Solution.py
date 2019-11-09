class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        res = 0
        for s in S:
            if s == '(':
                stack.append(res)
                res = 0
            else:
                res = stack.pop + max(res * 2, 1)

        return res

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for s in S:
            if stack and stack[-1] == '(' and s == ')':
                stack.pop()
            else:
                stack.append(s)
        return len(stack)
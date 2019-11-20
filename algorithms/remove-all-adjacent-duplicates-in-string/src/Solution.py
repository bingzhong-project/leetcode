class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

        res = ""
        while stack:
            res = stack.pop() + res

        return res

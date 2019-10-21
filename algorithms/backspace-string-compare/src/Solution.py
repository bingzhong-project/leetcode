class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(string):
            stack = []
            for s in string:
                if s == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(s)

            return str(stack)

        return build(S) == build(T)

class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack = []
        for e in pushed:
            stack.append(e)
            while popped and stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)

        if len(stack) != len(popped):
            return False
        for i in range(len(stack)):
            if stack[i] != popped[len(popped) - 1 - i]:
                return False

        return True

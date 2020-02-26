class Solution:
    def removeKdigits(self, num: 'str', k: 'int') -> 'str':
        stack = []
        del_count = 0
        for s in num:
            if del_count < k:
                while stack and stack[-1] > s and del_count < k:
                    stack.pop()
                    del_count += 1
            stack.append(s)
        while del_count < k and stack:
            stack.pop()
            del_count += 1
        res = 0
        while stack:
            n = int(stack.pop(0))
            res = res * 10 + n

        return str(res)

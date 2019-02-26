class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        stack = []
        res = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                cursor = stack.pop()
                res[cursor] = i - cursor
            stack.append(i)
        return res

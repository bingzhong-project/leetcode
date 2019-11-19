class Solution:
    def longestWPI(self, hours: list) -> int:
        sum_array = [0 for _ in range(len(hours) + 1)]
        for i in range(1, len(sum_array)):
            sum_array[i] = sum_array[i - 1] + (1 if hours[i - 1] > 8 else -1)
        stack = []
        for i in range(len(sum_array)):
            if not stack or sum_array[stack[-1]] > sum_array[i]:
                stack.append(i)

        res = 0
        for i in range(len(sum_array) - 1, -1, -1):
            while stack and sum_array[stack[-1]] < sum_array[i]:
                res = max(res, i - stack.pop())
        return res

class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        operator = {'+', '-', '*'}
        res = []
        for i in range(len(input)):
            if input[i] in operator:
                part1 = self.diffWaysToCompute(input[:i])
                part2 = self.diffWaysToCompute(input[i + 1:])
                for p1 in part1:
                    for p2 in part2:
                        if input[i] == '+':
                            res.append(p1 + p2)
                        elif input[i] == '-':
                            res.append(p1 - p2)
                        elif input[i] == '*':
                            res.append(p1 * p2)
        if len(res) == 0:
            res.append(int(input))
        return res

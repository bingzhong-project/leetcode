class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        counter = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for move in moves:
            counter[move] += 1
        return (counter['U'] == counter['D']) and (
            counter['L'] == counter['R'])

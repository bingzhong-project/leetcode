class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        pos = {'X': 0, 'Y': 0}
        X = {'L', 'R'}
        Y = {'U', 'D'}
        move_ops = {'L': -1, 'R': 1, 'U': -1, 'D': 1}
        for move in moves:
            if move in X:
                pos['X'] += move_ops[move]
            elif move in Y:
                pos['Y'] += move_ops[move]
        return pos['X'] == 0 and pos['Y'] == 0

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, s) for i, s in enumerate(dominoes) if s != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        res = list(dominoes)
        for (i, x), (j, y) in list(zip(symbols, symbols[1:])):
            if x == y:
                for k in range(i + 1, j):
                    res[k] = x
            elif x > y:
                for k in range(i + 1, j):
                    if k - i < j - k:
                        res[k] = x
                    elif k - i > j - k:
                        res[k] = y
                    else:
                        res[k] = '.'

        return ''.join(res)

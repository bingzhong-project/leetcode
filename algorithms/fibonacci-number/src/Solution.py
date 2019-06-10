class Solution:
    def __init__(self):
        self.fibnumber = {0: 0, 1: 1}

    def fib(self, N: 'int') -> 'int':
        if N in self.fibnumber:
            return self.fibnumber[N]
        res = self.fib(N - 2) + self.fib(N - 1)
        self.fibnumber[N] = res

        return res

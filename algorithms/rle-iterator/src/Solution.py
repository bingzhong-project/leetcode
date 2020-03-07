class RLEIterator:
    def __init__(self, A: list):
        self.stack = []
        for i in range(0, len(A), 2):
            self.stack.append([A[i + 1], A[i]])

    def next(self, n: int) -> int:
        res = -1
        while n > 0 and self.stack:
            top = self.stack[0]
            val = top[0]
            count = top[1]
            if count >= n:
                self.stack[0][1] = count - n
                n -= count
                res = val
            else:
                n -= count
                self.stack.pop(0)
        return res

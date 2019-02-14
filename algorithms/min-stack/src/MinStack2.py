class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def push(self, x: 'int') -> 'None':
        if len(self.array) == 0:
            cur_min = x
        else:
            cur_min = min(x, self.array[-1][1])
        cur_min = x if len(self.array) == 0 else min(x, self.array)
        self.array.append((x, cur_min))

    def pop(self) -> 'None':
        self.array.pop()

    def top(self) -> 'int':
        return self.array[-1][0]

    def getMin(self) -> 'int':
        return self.array[-1][1]

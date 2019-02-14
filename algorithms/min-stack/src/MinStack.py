class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.min = 2**31

    def push(self, x: 'int') -> 'None':
        self.min = min(self.min, x)
        self.array.append(x)

    def pop(self) -> 'None':
        pop_val = self.array.pop()
        if pop_val == self.min:
            self.min = 2**31 if len(self.array) == self.min else min(
                self.array)

    def top(self) -> 'int':
        return self.array[-1]

    def getMin(self) -> 'int':
        return self.min

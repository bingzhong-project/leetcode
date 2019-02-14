class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__array__ = []

    def push(self, x: 'int') -> 'None':
        if len(self.__array__) == 0:
            cur_min = x
        else:
            cur_min = min(x, self.__array__[-1][1])
        self.__array__.append((x, cur_min))

    def pop(self) -> 'None':
        self.__array__.pop()

    def top(self) -> 'int':
        return self.__array__[-1][0]

    def getMin(self) -> 'int':
        return self.__array__[-1][1]

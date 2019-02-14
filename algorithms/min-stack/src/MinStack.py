class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__array__ = []
        self.__min__ = 2**31

    def push(self, x: 'int') -> 'None':
        self.__min__ = min(self.__min__, x)
        self.__array__.append(x)

    def pop(self) -> 'None':
        pop_val = self.__array__.pop()
        if pop_val == self.__min__:
            if len(self.__array__) == 0:
                self.__min__ = 2**31
            else:
                self.__min__ = min(self.__array__)

    def top(self) -> 'int':
        return self.__array__[-1]

    def getMin(self) -> 'int':
        return self.__min__

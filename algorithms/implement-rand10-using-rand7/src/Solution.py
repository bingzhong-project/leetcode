import random


def rand7(self):
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        bin_str = ''
        for _ in range(4):
            bin_str += self.rand()
        res = int(bin_str, 2)
        return res if res > 0 and res <= 10 else self.rand10()

    def rand(self):
        num = rand7()
        if num < 4:
            return '1'
        elif num > 4:
            return '0'
        else:
            return self.rand()

import random


def rand7(self):
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand_num = (rand7() - 1) * 7 + rand7()
        return rand_num % 10 + 1 if rand_num <= 40 else self.rand10()

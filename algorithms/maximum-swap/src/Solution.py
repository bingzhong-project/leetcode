import collections


class Solution:
    def maximumSwap(self, num: 'int') -> 'int':
        array = []
        while num > 0:
            div, mod = divmod(num, 10)
            array.append(mod)
            num = div
        change = collections.defaultdict(list)
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] > array[j]:
                    change[array[i]] += [(i, j)]
        for i in range(10, 0, -1):
            if i in change:
                change[i].sort(key=lambda x: (x[0], -x[1]))
                m, n = change[i][0]
                temp = array[m]
                array[m] = array[n]
                array[n] = temp
                break

        res = 0
        for i in range(len(array)):
            res += array[i] * 10**i
        return res

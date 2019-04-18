import collections


class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        def binary(t_index_list, index, left, right):
            while left < right:
                mid = (left + right) // 2
                if t_index_list[mid] > index:
                    right = mid
                else:
                    left = mid + 1
            return t_index_list[left] if left < len(t_index_list) else -1

        table = collections.defaultdict(list)
        for i, v in enumerate(t):
            table[v] += [i]

        index = -1
        for v in s:
            if v not in table:
                return False
            index = binary(table[v], index, 0, len(table[v]))
            if index == -1:
                return False

        return True

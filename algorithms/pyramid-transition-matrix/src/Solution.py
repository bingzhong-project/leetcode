import collections


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list) -> bool:
        def func(cur, above, data):
            if len(cur) == 2 and len(above) == 1:
                return True
            if len(above) == len(cur) - 1:
                return func(above, "", data)
            pos = len(above)
            for string in data[cur[pos] + cur[pos + 1]]:
                if func(cur, above + string, data):
                    return True

            return False

        data = collections.defaultdict(list)
        for a in allowed:
            data[a[0] + a[1]] += [a[2]]

        return func(bottom, "", data)

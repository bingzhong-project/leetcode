import collections


class Solution:
    def leastBricks(self, wall: 'List[List[int]]') -> 'int':
        wall_length = sum(wall[0])
        counter = collections.Counter()
        counter[0] = 0
        for w in wall:
            ws = 0
            for i in range(len(w)):
                ws += w[i]
                if ws != wall_length:
                    counter[ws] += 1
        return len(wall) - max(list(counter.values()))

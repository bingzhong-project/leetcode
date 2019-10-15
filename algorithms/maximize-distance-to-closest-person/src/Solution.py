class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        res = 0
        pos = []
        for i in range(len(seats)):
            if seats[i] == 1:
                pos.append(i)
        for i in range(1, len(pos)):
            res = max(res, (pos[i] - pos[i - 1]) // 2)
        res = max(res, pos[0], len(seats) - pos[-1] - 1)
        return res

class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        res = 0
        pos = []
        for i in range(len(seats)):
            if seats[i] == 1:
                pos.append(i)
        if len(pos) == 1:
            res = max(pos[0], len(seats) - pos[0] - 1)
        else:
            for i in range(len(pos) - 1):
                res = max(res, (pos[i + 1] - pos[i]) // 2)
            res = max(res, pos[0], len(seats) - pos[-1] - 1)
        return res

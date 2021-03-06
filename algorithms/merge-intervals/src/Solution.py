# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1].end >= intervals[i].start:
                end = max(res[-1].end, intervals[i].end)
                res[-1] = Interval(res[-1].start, end)
            else:
                res.append(intervals[i])

        return res

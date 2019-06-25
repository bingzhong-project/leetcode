class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> 'int':
        MAX_MINUTES = 24 * 60
        times = []
        for point in timePoints:
            time = point.split(':')
            h = int(time[0])
            m = int(time[1])
            times.append(h * 60 + m)

        times.sort(reverse=True)
        min_diff = MAX_MINUTES
        for i in range(len(times) - 1):
            min_diff = min(min_diff, times[i] - times[i + 1])
        min_diff = min(min_diff, times[-1] + MAX_MINUTES - times[0])
        return min_diff

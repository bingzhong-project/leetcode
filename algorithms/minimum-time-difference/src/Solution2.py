class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> 'int':
        MAX_MINUTES = 24 * 60
        times = [0 for _ in range(MAX_MINUTES)]
        for point in timePoints:
            time = point.split(':')
            h = int(time[0])
            m = int(time[1])
            times[h * 60 + m] += 1
        min_index = None
        last_index = -MAX_MINUTES
        min_diff = MAX_MINUTES
        for i in range(len(times)):
            if times[i] > 0:
                if min_index is None:
                    min_index = i
                if times[i] > 1:
                    min_diff = 0
                else:
                    min_diff = min(min_diff, i - last_index)
                last_index = i

        return min(min_diff, min_index + MAX_MINUTES - last_index)

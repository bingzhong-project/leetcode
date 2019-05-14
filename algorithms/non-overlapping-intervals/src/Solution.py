class Solution:
    def eraseOverlapIntervals(self, intervals: 'List[List[int]]') -> 'int':
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda interval: interval[0])
        ans = 0
        left = 0
        right = 1
        while right < len(intervals):
            left_interval = intervals[left]
            right_interval = intervals[right]
            if left_interval[0] == right_interval[0]:
                ans += 1
                if left_interval[1] > right_interval[1]:
                    left = right
            elif left_interval[1] > right_interval[0]:
                ans += 1
                if left_interval[1] > right_interval[1]:
                    left = right
            else:
                left = right
            right += 1
        return ans

class Solution:
    def findRightInterval(self, intervals: 'List[List[int]]') -> 'List[int]':
        def search(prefix, num, left, right):
            if right - left == 1:
                return prefix[left][1] if prefix[left][0] >= num else prefix[
                    right][1]
            mid = (left + right) // 2
            if prefix[mid][0] > num:
                return search(prefix, num, left, mid)
            elif prefix[mid][0] < num:
                return search(prefix, num, mid, right)
            else:
                return prefix[mid][1]

        prefix = []
        for i in range(len(intervals)):
            prefix.append((intervals[i][0], i))
        prefix.sort()

        res = [-1 for _ in range(len(intervals))]
        for i in range(len(intervals)):
            suffix = intervals[i][1]
            if suffix <= prefix[-1][0]:
                res[i] = search(prefix, suffix, 0, len(prefix) - 1)
        return res

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort()
        result = 1
        end = points[0][1]
        for i in range(1, len(points)):
            point = points[i]
            if point[0] <= end:
                end = min(end, point[1])
            else:
                result += 1
                end = point[1]

        return result

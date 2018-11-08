class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = 0
        while left != right:
            left_side = height[left]
            right_side = height[right]
            side = min(left_side, right_side)
            result = max(result, side * (right - left))
            if left_side <= right_side:
                left = left + 1
            else:
                right = right - 1
        return result

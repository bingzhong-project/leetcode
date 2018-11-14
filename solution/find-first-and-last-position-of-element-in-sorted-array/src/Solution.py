class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(array, target, start, end, result):
            if start > end:
                return
            mid = int((start + end) / 2)
            num = array[mid]
            if num > target:
                search(array, target, start, mid - 1, result)
            elif num < target:
                search(array, target, mid + 1, end, result)
            else:
                if result[0] == -1 or mid < result[0]:
                    result[0] = mid
                if result[0] == -1 or mid > result[1]:
                    result[1] = mid
                search(array, target, start, mid - 1, result)
                search(array, target, mid + 1, end, result)

        result = [-1, -1]
        search(nums, target, 0, len(nums) - 1, result)
        return result

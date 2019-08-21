import collections


class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        counter = collections.Counter(nums)
        degree_nums = []
        degree = 0
        for key, count in counter.items():
            if count > degree:
                degree_nums = [key]
                degree = count
            elif count == degree:
                degree_nums.append(key)
        if degree == 1:
            return 1
        res = len(nums)
        for degree_num in degree_nums:
            left = 0
            right = len(nums) - 1
            find_left = False
            find_right = False
            while left < right:
                find_left = nums[left] == degree_num
                find_right = nums[right] == degree_num
                if find_left and find_right:
                    break
                if not find_left:
                    left += 1
                if not find_right:
                    right -= 1
            res = min(res, right - left + 1)
        return res

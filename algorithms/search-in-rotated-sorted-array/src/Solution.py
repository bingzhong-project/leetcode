class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_min(nums, start, end, min_cursor=[0], min_result=[2**31]):
            if start == end:
                if nums[start] < min_result[0]:
                    min_cursor[0] = start
                    min_result[0] = nums[start]
                return min_cursor[0]
            mid = int((start + end) / 2)
            find_min(nums, start, mid, min_cursor, min_result)
            find_min(nums, mid + 1, end, min_cursor, min_result)
            return min_cursor[0]

        def get_real_cursor(relative_cursor, offset, length):
            relative_cursor += offset
            if relative_cursor >= length:
                relative_cursor -= length
            return relative_cursor

        def search_target(nums, start, end, offset, target):
            if end - start <= 1:
                if target == nums[get_real_cursor(start, offset, len(nums))]:
                    return get_real_cursor(start, offset, len(nums))
                elif target == nums[get_real_cursor(end, offset, len(nums))]:
                    return get_real_cursor(end, offset, len(nums))
                return -1
            mid = int((start + end) / 2)
            real_mid_cursor = get_real_cursor(mid, offset, len(nums))
            if target < nums[real_mid_cursor]:
                return search_target(nums, start, mid, offset, target)
            elif target > nums[real_mid_cursor]:
                return search_target(nums, mid, end, offset, target)
            else:
                return real_mid_cursor

        if len(nums) == 0:
            return -1
        else:
            min_cursor = find_min(nums, 0, len(nums) - 1)
            return search_target(nums, 0, len(nums) - 1, min_cursor, target)
